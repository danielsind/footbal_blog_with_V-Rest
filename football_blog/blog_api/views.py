from django.shortcuts import render
from .models import Post
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from serializers import PostSerializer


@api_view (['GET', 'POST'])
def post_list(request, format=None):

    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
