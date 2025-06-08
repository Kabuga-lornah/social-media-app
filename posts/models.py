from django.db import models
from accounts.models import CustomUser
from cloudinary.models import CloudinaryField

class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(CustomUser, related_name='liked_posts', blank=True)

    def __str__(self):
        return f"Post by {self.user.username} at {self.created_at}"