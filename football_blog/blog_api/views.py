from django.shortcuts import render
from .models import Post
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework import status
from serializers import PostSerializer

class PostAPIView(APIView):
    def get(self, request: Request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request: Request): 
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request: Request, pk):
        instance = self.get_object(pk)
        serializer = PostSerializer(instance)
        return Response(serializer.data)

    def put(self, request: Request, pk):
        instance = self.get_object(pk)
        serializer = PostSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk):
        instance = self.get_object(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class FilteredPostsAPIView(APIView):
    def get(self, request):
        queryset = Post.objects.all()

        # Apply filters
        title = request.query_params.get('title')
        author = request.query_params.get('author')
        content = request.query_params.get('content')
        category = request.query_params.get('category')

        if title:
            queryset = queryset.filter(title__icontains=title)
        if author:
            queryset = queryset.filter(author__icontains=author)
        if content:
            queryset = queryset.filter(category__icontains=content)
        if category:
            queryset = queryset.filter(category__icontains=category)

        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CategoryPostsAPIView(APIView):
    def get(self, request: Request, category: str):
        posts = Post.objects.filter(category=category)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)