from django.urls import path
from blog_api import views as blog_api_views
from user_api import views as user_api_views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from django.urls import include

app_name="blog"
router = DefaultRouter()
router.include_format_suffixes = False
router.register(r'users', user_api_views.UserListView, basename='UserListView')

urlpatterns = [
    path('posts/', blog_api_views.PostAPIView.as_view(), name='posts'),
    path('posts/<int:id>', blog_api_views.PostDetailView.as_view(), name='post-detail'),
     path('filter/', blog_api_views.FilteredPostsAPIView.as_view(), name='filtered_posts_api'),
     # test with this /filter/?q=search_query
    path('category/<str:category>', blog_api_views.CategoryPostsAPIView.as_view(), name='category'),
    # path('register/',user_api_views.UserRegistrationView.as_view(), name='user-registration'),
    # path('login/', user_api_views.UserLoginView.as_view(), name='user-login'),
    path('', include(router.urls)),
    # path('', user_api_views.UserListView.as_view(), name='user-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

