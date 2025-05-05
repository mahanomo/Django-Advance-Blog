from rest_framework import serializers
from accounts.models import User,Profile
from django.core import exceptions
import django.contrib.auth.password_validation as validators
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=100,write_only=True)
    class Meta:
        model = User
        fields=['email','password','confirm_password']

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError({'detail':"passwords dosn't match!"})
        
        errors = {}
        try:
            # validate the complexity of password
            validators.validate_password(attrs.get('password'))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'password':list(e.messages)})
            
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        return User.objects.create_user(**validated_data)


# overwrite token serializer class
class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(
        label=_("email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        username = attrs.get('email')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


from rest_framework import serializers
from django.contrib.auth.models import User

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password2 = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs.get('new_password') != attrs.get('new_password2'):
            raise serializers.ValidationError({'detail':"passwords dosn't match!"})
        
        errors = {}
        try:
            # validate the complexity of password
            validators.validate_password(attrs.get('new_password'))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'new_password':list(e.messages)})
            
        return super().validate(attrs)
    

class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', read_only=True)
   
    class Meta:
        model = Profile
        fields=['id','email','first_name','last_name','descreaption']