from django.urls import path, include

# set name for app
app_name = "accounts"
# write paths here

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("api/v1/", include("accounts.api.v1.urls")),
]
