from .models import Post
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework import status
from serializers import PostSerializer
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly

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

class PostDetailView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_post(self, post_id):
        try:
            return Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, post_id):
        post = self.get_post(post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, post_id):
        post = self.get_post(post_id)
        
        # Check if the user is the owner of the post
        if post.user != request.user:
            raise PermissionDenied("You do not have permission to update this post.")

        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_id):
        post = self.get_post(post_id)
        
        # Check if the user is the owner of the post
        if post.user != request.user:
            raise PermissionDenied("You do not have permission to delete this post.")

        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class FilteredPostsAPIView(APIView):
    def get(self, request, q):
        queryset = Post.objects.all()

        # Apply filters
        query = q
        # author = request.query_params.get('author')
        # content = request.query_params.get('content')
        # category = request.query_params.get('category')

        # if title:
        #     queryset = queryset.filter(title__icontains=title)
        # if author:
        #     queryset = queryset.filter(author__icontains=author)
        # if content:
        #     queryset = queryset.filter(category__icontains=content)
        if query:
            queryset = queryset.filter(category__icontains=query)

        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CategoryPostsAPIView(APIView):
    def get(self, request: Request, category:str):
        posts = Post.objects.filter(category=category)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)