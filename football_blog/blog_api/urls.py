from django.urls import path
from .import views
from blog_api import views
from user_api import views as user_api_views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('posts/', views.post_list),
    path('posts/<int:id>', views.post_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
