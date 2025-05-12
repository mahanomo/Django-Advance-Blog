from django.urls import path
from .. import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    # registration
    path(
        "registration/",
        views.RegistrationApiView.as_view(),
        name="registration",
    ),
    # verification and resend verification
    path(
        "activation/confirm/<str:token>",
        views.ActivationApiView.as_view(),
        name="activation",
    ),
    path(
        "activation/resend/",
        views.ActivationResendApiView.as_view(),
        name="resend-activation",
    ),
    # login and generate token
    path("token/login/", views.CustomAuthToken.as_view(), name="login-token"),
    # logout and destory token
    path("token/logout/", views.CustomLogout.as_view(), name="logout-token"),
    # change password
    path(
        "change_password/",
        views.ChangePasswordView.as_view(),
        name="change-password",
    ),
    # jwt login
    path("jwt/create/", TokenObtainPairView.as_view(), name="jwt-create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt-verify"),
]
