from django.db import models
from accounts.models import CustomUser
from posts.models import Post

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(CustomUser, related_name='liked_comments', blank=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post}"
