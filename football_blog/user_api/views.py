from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from blog_api.models import Post
from user_api.models import UserProfile 
from serializers import UserSerializer, PostSerializer, UserProfileSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from rest_framework.exceptions import PermissionDenied
from django.urls import reverse

class UserListView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'detail': 'Login successful'}, status=status.HTTP_200_OK)
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['post'])
    def logout(self, request):
        logout(request)
        return Response({'detail': 'Logout successful'}, status=status.HTTP_200_OK)

    # def list(self, request, *args, **kwargs):
    #     # Implement login functionality
    #     username = request.query_params.get('username')
    #     password = request.query_params.get('password')
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return Response({'detail': 'Login successful'}, status=status.HTTP_200_OK)
    #     return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    # def destroy(self, request, *args, **kwargs):
    #     # Implement logout functionality
    #     logout(request)
    #     return Response({'detail': 'Logout successful'}, status=status.HTTP_200_OK)



class UserProfileView(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
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

# class UserProfileDetailView(APIView):
#     permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

#     def get_user(self, user_id):
#         try:
#             return UserProfile.objects.get(id=user_id)
#         except UserProfile.DoesNotExist:
#             raise status.HTTP_404_NOT_FOUND

#     def get(self, request, user_id):
#         user = self.get_user(user_id)
#         serializer = UserProfileSerializer(user)
#         return Response(serializer.data)

#     def put(self, request, user_id):
#         user = self.get_user(user_id)
        
#         # Check if the user is the owner of the post
#         if user.user != request.user:
#             raise PermissionDenied("You do not have permission to update this Profile.")

#         serializer = UserProfileSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, user_id):
#         user = self.get_user(user_id)
        
#         # Check if the user is the owner of the post
#         if user.user != request.user:
#             raise PermissionDenied("You do not have permission to delete this Profile.")

#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserPostsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        # Retrieve the user's posts
        user_posts = Post.objects.filter(user_id=user_id)
        serializer = PostSerializer(user_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    