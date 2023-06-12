from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from blog_api.models import Post
from user_api.models import UserProfile 
from serializers import UserSerializer, PostSerializer, UserProfileSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from rest_framework.exceptions import PermissionDenied
class UserAPIView(APIView):
    def get(self, request: Request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def register(self, request: Request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UserProfileDetailView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_user(self, user_id):
        try:
            return UserProfile.objects.get(id=user_id)
        except UserProfile.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, user_id):
        user = self.get_user(user_id)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

    def put(self, request, user_id):
        user = self.get_user(user_id)
        
        # Check if the user is the owner of the post
        if user.user != request.user:
            raise PermissionDenied("You do not have permission to update this Profile.")

        serializer = UserProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        user = self.get_user(user_id)
        
        # Check if the user is the owner of the post
        if user.user != request.user:
            raise PermissionDenied("You do not have permission to delete this Profile.")

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserPostsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        # Retrieve the user's posts
        user_posts = Post.objects.filter(user_id=user_id)
        serializer = PostSerializer(user_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    