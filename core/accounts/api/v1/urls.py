from django.urls import path
from . import views
from rest_framework import routers
# from rest_framework.authtoken import views as view

#set name for app
app_name = "api-v1"
#write paths here

router = routers.DefaultRouter()



urlpatterns = [
    # registration
    path('registration/', views.RegistrationApiView.as_view() ,name="registration"),
    path('login/', views.CustomAuthToken.as_view())

]