from django.urls import path
from . import views

#set name for app
app_name = "api-v1"
#write paths here

urlpatterns = [
    # path("posts/", views.postsList,name="posts-list"),
    path("posts/", views.PostsList.as_view(),name="posts-list"),
    path("posts/<int:id>", views.postsDetail,name="posts-detial"),
]

