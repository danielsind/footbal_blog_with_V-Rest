from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from PIL import Image


def validate_video_file(value):
    allowed_extensions = ['.mp4', '.avi', '.mov']
    if not value.name.lower().endswith(tuple(allowed_extensions)):
        raise ValidationError("Only video files are allowed.")

def validate_image_format(post_image):
    try:
        image = Image.open(post_image)

        allowed_formats = ['JPEG', 'PNG', 'GIF', 'JPG']
        if image.format not in allowed_formats:
            raise ValidationError("Invalid image format. Only JPEG, PNG, and GIF are allowed.")

    except Exception:
        raise ValidationError("Unable to open the image file.")

class Post(models.Model):

    CATEGORY_CHOICES = (
        ('general', 'General'),
        ('leagues', 'Leagues'),
        ('players highlights', 'Players highlights'),
        ('latest news', 'Latest News'),
        ('videos', 'Videos'),
    )

    IMAGE = 'post_image'
    VIDEO = 'video_file'
    CHOICES = (
        (IMAGE, 'post_image'),
        (VIDEO, 'Video_file'),
    )


    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    post_image = models.ImageField(default='default.jpg', upload_to='post_image_pics', validators=[], null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='general')
    video_file = models.FileField(upload_to='videos/', default='default_video.mp4', validators=[validate_video_file], null=True, blank=True)

    # def clean(self):
    #     # Ensure that only one field (image or video) is filled
    #     if self.post_image and self.video_file:
    #         raise ValidationError("Only one of image or video should be provided.")
        
    #     if not self.post_image and not self.video_file:
    #         raise ValidationError("Either image or video should be provided.")

    def __str__(self):
            return self.title
    
    