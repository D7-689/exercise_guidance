from django.contrib.auth.models import User
from django.db import models
import time
import os

def content_file_name(instance, filename):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    name, extension = os.path.splitext(filename)
    return os.path.join('content', instance.user.username, timestr + extension)

class UserFaceImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=content_file_name, blank=False)

class Learner(models.Model):                                    #Self-declare model
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    image = models.ImageField(default='default.png',null=True,blank=True)             #upload_to='static/images'

    def __str__(self):
        return f"{self.user.username} Profile"