# Generated by Django 4.2.2 on 2023-06-09 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(default='default.jpg', upload_to='post_image_pics'),
        ),
    ]
