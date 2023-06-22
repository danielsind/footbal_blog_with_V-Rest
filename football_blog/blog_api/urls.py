from django.urls import path, include
from blog_api import views as blog_api_views
from rest_framework import routers
from user_api import views as user_api_views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


app_name="blog"
router = routers.DefaultRouter()
router.register(r'posts', blog_api_views.PostListView, basename='posts')
router.register(r'users', user_api_views.UserListView, basename='users')
router.register(r'user-profile', user_api_views.UserProfileView, basename='user-profile')


router.include_format_suffixes = False 

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

