from django.urls import path
from . import views
from rest_framework import routers

#set name for app
app_name = "api-v1"
#write paths here

router = routers.DefaultRouter()
router.register('posts', views.PostModelViewSet, basename='p-modelviewset')
router.register('category', views.CategoryModelViewSet, basename='c-modelviewset')
urlpatterns = router.urls


"""urlpatterns = [
    # path("posts/", views.postsList,name="posts-list"),
    # path("posts/", views.ListCreateAPIView.as_view(),name="posts-list"),
    # path("posts/<int:pk>", views.RetrieveUpdateDestroyAPIView.as_view(),name="posts-detial"),
    path("posts/", views.ModelViewSet.as_view({'get': 'list'}),name="posts-list"),
    path("posts/<int:pk>", views.ModelViewSet.as_view({'get': 'retrieve',
                                                       "post":"create",
                                                       "put":"update",
                                                       "patch":"partial_update"
                                                       ,"delete":"destroy"}),name="posts-detial"),

]"""

