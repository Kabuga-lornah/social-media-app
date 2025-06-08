from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField

class CustomUser(AbstractUser):
    profile_picture = CloudinaryField('image', blank=True, null=True)
    bio = models.TextField(blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')

    def __str__(self):
        return self.username
    