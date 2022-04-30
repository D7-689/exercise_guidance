import django
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator   # Use in User_height_weightform
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

class User_Weight_Height(models.Model):
    gender_choice = (
        ('F', 'Female',),
        ('M', 'Male',),
    )
    user =  models.OneToOneField(User, on_delete=models.CASCADE,related_name='person_info')
    height = models.PositiveIntegerField(validators=[MaxValueValidator(250)],null=True)
    weight = models.PositiveIntegerField(validators=[MaxValueValidator(400)],null=True)
    age = models.PositiveIntegerField(validators=[MaxValueValidator(100)],null=True)
    gender = models.CharField(max_length=1,choices=gender_choice,null=True)

 