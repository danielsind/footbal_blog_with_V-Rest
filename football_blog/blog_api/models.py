from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from PIL import Image


def validate_video_file(value):
    # Custom validation to ensure the uploaded file is a video
    # You can implement your own validation logic here
    # For example, check the file extension or use external libraries

    # Sample validation using file extension
    allowed_extensions = ['.mp4', '.avi', '.mov']
    if not value.name.lower().endswith(tuple(allowed_extensions)):
        raise ValidationError("Only video files are allowed.")
# Create your models here.
class Post(models.Model):
    CATEGORY_CHOICES = (
        ('general', 'General'),
        ('leagues', 'Leagues'),
        ('players highlights', 'Players highlights'),
        ('latest news', 'Latest News'),
        ('videos', 'Videos'),
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    post_image = models.ImageField(default='default.jpg', upload_to='post_image_pics')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='general')
    video_file = models.FileField(upload_to='videos/',validators=[validate_video_file], default='default_video.mp4')

    def __str__(self):
            return self.title
    
    