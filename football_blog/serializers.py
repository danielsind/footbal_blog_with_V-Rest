from rest_framework import serializers
from blog_api.models import Post
from user_api.models import UserProfile
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author','post_image','category']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        field = ['id', 'user','image',]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'