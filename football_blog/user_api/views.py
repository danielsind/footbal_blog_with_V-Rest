from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login, logout
from blog_api.models import Post
from user_api.models import UserProfile 
from serializers import UserSerializer, PostSerializer, UserProfileSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from rest_framework.exceptions import PermissionDenied
from django.urls import reverse
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import action

class UserListView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class LoginView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user:
#             refresh = RefreshToken.for_user(user)
#             token = {
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             }
#             return Response(token, status=status.HTTP_200_OK)

#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
  
    # def get_permissions(self):
    #     if self.action in ['put', 'delete']:
    #         permission_classes = [IsAuthenticated]
    #     else:
    #         permission_classes = []
    #     return [permission() for permission in permission_classes]
    
    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # @action(methods=['get'], detail=True)
    # def get(self, request, *args, **kwargs):
    #     self.authentication_classes = [JWTAuthentication]
    #     user = request.user
    #     # Your implementation here
    #     if user.is_authenticated:
    #         # Process the authenticated user's request
    #         return Response({'message': 'Authenticated user GET request'})
    #     else:
    #         # Process unauthenticated user's request
    #         return Response({'message': 'Unauthenticated user GET request'})

    # @action(methods=['put'], detail=True)
    # def put(self, request, *args, **kwargs):
    #     self.authentication_classes = [JWTAuthentication]
    #     user = request.user
    #     # Your implementation here
    #     if user.is_authenticated:
    #         # Process the authenticated user's request
    #         return Response({'message': 'Authenticated user PUT request'})
    #     else:
    #         # Return 403 Forbidden for unauthenticated user's request
    #         return Response(status=status.HTTP_403_FORBIDDEN)

    # @action(methods=['delete'], detail=True)
    # def delete(self, request, *args, **kwargs):
    #     self.authentication_classes = [JWTAuthentication]
    #     user = request.user
    #     # Your implementation here
    #     if user.is_authenticated:
    #         # Process the authenticated user's request
    #         return Response({'message': 'Authenticated user DELETE request'})
    #     else:
    #         # Return 403 Forbidden for unauthenticated user's request
    #         return Response(status=status.HTTP_403_FORBIDDEN)


# class RegisterView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


# class LoginView(APIView):

#     def post(self, request):
#         email = request.data['email']
#         password = request.data['password']

#         user = User.objects.filter(email=email).first()

#         if user is None:
#             raise AuthenticationFailed('User not found!')

#         if not user.check_password(password):
#             raise AuthenticationFailed('Incorrect password!')

#         payload = {
#             'id': user.id,
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
#             'iat': datetime.datetime.utcnow()
#         }

#         token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

#         response = Response()

#         response.set_cookie(key='jwt', value=token, httponly=True)
#         response.data = {
#             'jwt': token
#         }
#         return response


# class UserView(APIView):

#     def get(self, request):
#         token = request.COOKIES.get('jwt')

#         if not token:
#             raise AuthenticationFailed('Unauthenticated!')

#         try:
#             payload = jwt.decode(token, 'secret', algorithm=['HS256'])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Unauthenticated!')

#         user = User.objects.filter(id=payload['id']).first()
#         serializer = UserSerializer(user)
#         return Response(serializer.data)

# class LogoutView(APIView):

#     def post(self, request):
#         response = Response()
#         response.delete_cookie('jwt')
#         response.data = {
#             'message': 'success'
#         }
#         return response

    # @action(detail=False, methods=['post'])
    # def login(self, request):
    #     username = request.data.get('username')
    #     password = request.data.get('password')
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return Response({'detail': 'Login successful'}, status=status.HTTP_200_OK)
    #     return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    # @action(detail=False, methods=['post'])
    # def logout(self, request):
    #     logout(request)
    #     return Response({'detail': 'Logout successful'}, status=status.HTTP_200_OK)

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
    
# class UserPostsAPIView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, user_id):
#         # Retrieve the user's posts
#         user_posts = Post.objects.filter(user_id=user_id)
#         serializer = PostSerializer(user_posts, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
    