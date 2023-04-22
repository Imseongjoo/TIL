from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings


# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_posts')
    title = models.CharField(max_length=20)
    select1_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='selected1_users', blank=True)
    select1_content = models.CharField(max_length=20)
    select2_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='selected2_users', blank=True)
    select2_content = models.CharField(max_length=20)
    image1 = ProcessedImageField(blank=True, null=True,
                                 upload_to='image/',
                                 processors=[ResizeToFill(260, 300)],
                                 format='JPEG',
                                 options={'quality': 90})
    image2 = ProcessedImageField(blank=True, null=True,
                                 upload_to='image/',
                                 processors=[ResizeToFill(260, 300)],
                                 format='JPEG',
                                 options={'quality': 90})


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
