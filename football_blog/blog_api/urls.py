from django.urls import path, include
from blog_api import views as blog_api_views
from rest_framework import routers
from user_api import views as user_api_views
from rest_framework.urlpatterns import format_suffix_patterns

app_name="blog"
router = routers.DefaultRouter()
router.register(r'posts', blog_api_views.PostListView, basename='posts')
router.register(r'users', user_api_views.UserListView, basename='users')
router.register(r'user-profile', user_api_views.UserProfileView, basename='user-profile')


router.include_format_suffixes = False 

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)

