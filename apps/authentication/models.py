from django.contrib.auth.models import User
from django.db import models


class profile_pics(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, default='profile_pics/default.png')
