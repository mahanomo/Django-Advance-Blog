from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from blog.models import Post
from django.shortcuts import get_object_or_404
from rest_framework import status

@api_view(["GET","POST"])
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