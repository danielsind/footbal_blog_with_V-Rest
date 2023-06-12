from django.urls import path
from blog_api import views as blog_api_views
from user_api import views as user_api_views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('posts/', blog_api_views.PostAPIView.as_view(), name='posts'),
    path('posts/<int:id>', blog_api_views.PostDetailView.as_view(), name='post-detail'),
    path('filter-posts', blog_api_views.FilteredPostsAPIView.as_view(), name='filter-posts'),
    path('category/<str:category>', blog_api_views.CategoryPostsAPIView.as_view(), name='category'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

