from django.contrib import admin
from .models import Learner , UserFaceImage, User_Weight_Height


# Register your models here.
admin.site.register(Learner)
# Add for the face login model
admin.site.register(UserFaceImage)
# Add for the User height and weight model
admin.site.register(User_Weight_Height)