from django.urls import path, include
from blog_api import views as blog_api_views
from rest_framework import routers
from user_api import views as user_api_views
from rest_framework.urlpatterns import format_suffix_patterns

app_name="blog"
router = routers.DefaultRouter()
router.register(r'posts', blog_api_views.PostListView, basename='posts')
router.register(r'users', user_api_views.UserListView, basename='users')
# router.register(r'posts/filter/<str:q>', blog_api_views.FilteredPostsAPIView, basename='posts-filter')
router.include_format_suffixes = False 
# router.register(r'users', user_api_views.UserListView, basename='UserListView')

urlpatterns = [
    # path('posts/', blog_api_views.PostAPIView.as_view(), name='posts'),
    # path('posts-detail/<int:id>', blog_api_views.PostDetailView.as_view(), name='post-detail'),
    # path('filter/', blog_api_views.FilteredPostsAPIView.as_view(), name='filtered_posts_api'),
     # test with this //?q=search_query
    path('', include(router.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)

