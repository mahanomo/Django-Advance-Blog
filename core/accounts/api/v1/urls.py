from django.urls import path
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView)
# from rest_framework.authtoken import views as view

#set name for app
app_name = "api-v1"
#write paths here

router = routers.DefaultRouter()



urlpatterns = [    
    
    # registration
    path('registration/', views.RegistrationApiView.as_view() ,name='registration'),
    
    # login and generate token
    path('token/login/', views.CustomAuthToken.as_view(),name='login-token'),
    
    # logout and destory token
    path('token/logout/', views.CustomLogout.as_view(),name='logout-token'),
    
    # change password
    path('change_password/',views.ChangePasswordView.as_view(),name="change-password"),
    
    # jwt login
    path('jwt/create/', TokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify'),

    # profile
    path('profile/',views.ProfileApiView.as_view(),name='profile'),
]