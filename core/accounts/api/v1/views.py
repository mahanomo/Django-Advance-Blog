from rest_framework import generics, status
from .serializers import (
    RegistrationSerializer,
    CustomAuthTokenSerializer,
    ChangePasswordSerializer,
    ProfileSerializer,
    ResendActivationSerializer,
)
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from accounts.models import Profile
from django.shortcuts import get_object_or_404
from mail_templated import EmailMessage
from ..utils import EmailThread
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidSignatureError
from django.conf import settings

User = get_user_model()


class RegistrationApiView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data["email"]
            data = {"email": email}
            user_obj = get_object_or_404(User, email=email)
            token = self.get_tokens_for_user(user_obj)
            email_obj = EmailMessage(
                "email/activation.tpl",
                {"token": token},
                "admin@admin.com",
                to=[email],
            )
            EmailThread(email_obj).start()

            return Response(data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


class CustomAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user_id": user.pk, "email": user.email})


class CustomLogout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChangePasswordView(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = [IsAuthenticated]

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                "status": "success",
                "code": status.HTTP_200_OK,
                "message": "Password updated successfully",
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileApiView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = get_object_or_404(Profile, user=self.request.user)
        return obj


class ActivationApiView(APIView):

    def get(self, request, token, *args, **kwargs):
        try:
            decodedPayload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=["HS256"]
            )
            user_id = decodedPayload.get("user_id")
        except ExpiredSignatureError:
            return Response({"details": "your token is exp"})
        except InvalidSignatureError:
            return Response({"details": "your token is invalid"})

        user_obj = User.objects.get(pk=user_id)

        if user_obj.is_verified:
            return Response({"details": "you are verified"})

        user_obj.is_verified = True
        user_obj.save()
        return Response({"details": "you have been successfully verified now!"})


class ActivationResendApiView(generics.GenericAPIView):
    serializer_class = ResendActivationSerializer

    def post(self, request, *args, **kwargs):
        serializer = ResendActivationSerializer(data=request.data)
        if serializer.is_valid():
            user_obj = serializer.validated_data["user"]
            token = self.get_tokens_for_user(user_obj)
            email_obj = EmailMessage(
                "email/activation.tpl",
                {"token": token},
                "admin@admin.com",
                to=[user_obj.email],
            )
            EmailThread(email_obj).start()

            return Response(
                {"detial": "resend activation to email successfully!"},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"detial": "resend activation to email failed!"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
