from django.urls import path, include
from . import views
from django.views.generic.base import RedirectView

# set name for app
app_name = "blog"
# write paths here

urlpatterns = [
    path("cbv/", views.IndexView.as_view(), name="index"),
    path(
        "go-to-django/",
        RedirectView.as_view(pattern_name="blog:index"),
        name="go-to-django",
    ),
    path("posts/", views.PostsListView.as_view(), name="posts"),
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("posts/create/", views.AuthorCreateView.as_view(), name="post-create"),
    path("posts/<int:pk>/update", views.PostUpdateView.as_view(), name="post-update"),
    path("posts/<int:pk>/delete", views.PostDeleteView.as_view(), name="post-delete"),
    path("api/v1/", include("blog.api.v1.urls")),
]
