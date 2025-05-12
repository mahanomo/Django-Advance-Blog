# from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    # IsAuthenticated,
)

# from rest_framework.response import Response
# from rest_framework.views import APIView
from .serializers import PostSerializer, CategorySerializer
from blog.models import Post, Category

# from django.shortcuts import get_object_or_404
# from rest_framework import status
# from django.core.exceptions import ValidationError
from rest_framework import mixins
from rest_framework.generics import GenericAPIView

# from rest_framework.viewsets import GenericViewSet
# from django.http import Http404
from rest_framework import viewsets

# from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .pagination import CustomPagination

"""
@api_view(["GET","POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def postsList(request):
    if request.method == "GET":
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        """

"""class PostsList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self,request):
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""


class ListCreateAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):

    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


"""
@api_view(["GET","PUT","DELETE"])
def postsDetail(request,id):

    posts = get_object_or_404(Post,pk=id)
    if request.method == "GET":
        serializer = PostSerializer(posts)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = PostSerializer(posts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        posts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    """


"""class PostsDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    def get(self,request,id):
        posts = get_object_or_404(Post,pk=id)
        serializer = PostSerializer(posts)
        return Response(serializer.data)
    def put(self,request,id):
        posts = get_object_or_404(Post,pk=id)
        serializer = PostSerializer(posts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        posts = get_object_or_404(Post,pk=id)
        posts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)"""


class RetrieveUpdateDestroyAPIView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView,
):
    """
    Concrete view for retrieving, updating or deleting a model instance.
    """

    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


"""class PostViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def list(self, request):
        queryset = Post.objects.filter(status=True)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        queryset = Post.objects.filter(status=True)
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    def create(self, request):
        pass
    def update(self, request, pk=None):
        pass
    def partial_update(self, request, pk=None):
        pass
    def destroy(self, request, pk=None):
        pass
"""


class PostModelViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Post.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["title", "content"]
    filterset_fields = {
        "category": ["exact", "in"],
        "author": ["exact", "in"],
        "status": ["exact", "in"],
    }
    ordering_fields = ["published_date"]
    pagination_class = CustomPagination


class CategoryModelViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Post.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
