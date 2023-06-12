from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from blog_api.models import Post
from user_api.models import UserProfile 
from serializers import UserSerializer, PostSerializer, UserProfileSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class UserAPIView(APIView):
    def get(self, request: Request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request: Request, pk):
        instance = self.get_object(pk)
        serializer = UserSerializer(instance)
        return Response(serializer.data)

    def put(self, request: Request, pk):
        instance = self.get_object(pk)
        serializer = UserSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk):
        instance = self.get_object(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserPostsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        # Retrieve the user's posts
        user_posts = Post.objects.filter(user_id=user_id)
        serializer = PostSerializer(user_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, user_id):
        # Create a new post for the user
        request.data['user_id'] = user_id
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)