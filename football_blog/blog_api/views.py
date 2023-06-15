from .models import Post
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from serializers import PostSerializer
# from rest_framework.exceptions import PermissionDenied
# from rest_framework.permissions import IsAuthenticated
# from .permissions import IsOwnerOrReadOnly
from django.db.models import Q

class PostListView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self, *args, **kwargs):
        query_list = Post.objects.all()
        query = self.request.GET.get("q")
        if query:
            query_list = query_list.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            ).distinct()
        return query_list
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)
        
        return queryset

    
