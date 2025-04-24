from django.urls import path
from . import views
from django.views.generic.base import RedirectView

#set name for app
app_name = "blog"
#write paths here

urlpatterns = [
    path("cbv/",views.IndexView.as_view(), name="index"),
    path("go-to-django/", RedirectView.as_view(pattern_name ="blog:index"), name="go-to-django",),
    path("posts/", views.PostsListView.as_view()),
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("posts/create/", views.AuthorCreateView.as_view(), name="post-create"),
]
