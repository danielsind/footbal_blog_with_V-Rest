from rest_framework import serializers
from football_blog.blog_api.models import Post
from football_blog.user_api.models import Profile

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author','post_image']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        field = ['id', 'user','image']