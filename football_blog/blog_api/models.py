from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    post_image = models.ImageField(default='default.jpg', upload_to='post_image_pics')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
            return self.title
    