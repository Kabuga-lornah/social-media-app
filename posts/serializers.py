from rest_framework import serializers
from .models import Post
from accounts.serializers import UserProfileSerializer

class PostSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    likes_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ('id', 'user', 'content', 'image', 'created_at', 'updated_at', 'likes_count', 'is_liked')
    
    def get_likes_count(self, obj):
        return obj.likes.count()
    
    def get_is_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(id=request.user.id).exists()
        return False