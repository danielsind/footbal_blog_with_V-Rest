from django.db import models
from blog_api.models import Post

from django.db import models
from django.contrib.auth.models import User
from PIL import Image 

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    posts = models.ManyToManyField(Post)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def update_posts(self):
        self.posts.set(Post.objects.filter(author=self.user))


def __str__(self):
    return f'{self.username} Profile'

def save(self, *args, **kwargs):
    super(UserProfile).save(*args, **kwargs)

    img = Image.open(self.image.path)

    if img.height > 300 or img.width > 300:
        output_size = (300, 300)
        img.thumbnail(output_size)
        img.save(self.image.path)