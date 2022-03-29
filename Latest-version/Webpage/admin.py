from django.contrib import admin
from .models import Learner , UserFaceImage


# Register your models here.
admin.site.register(Learner)
# Add for the face login model
admin.site.register(UserFaceImage)