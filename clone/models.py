from django.db import models
from django.contrib.auth.models import User

class SocialPost(models.Model):
    user_id = models.ForeignKey(User, verbose_name='USER',on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Picture')
    description = models.CharField(max_length=300, verbose_name='Description')
    likes = models.IntegerField(default=0, verbose_name='Likes')