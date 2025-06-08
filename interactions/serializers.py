from rest_framework import serializers
from .models import Comment
from accounts.serializers import UserProfileSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    likes_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = ('id', 'user', 'post', 'content', 'created_at', 'updated_at', 'likes_count', 'is_liked')
    
    def get_likes_count(self, obj):
        return obj.likes.count()
    
    def get_is_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(id=request.user.id).exists()
        return False