from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
from posts.models import Post
from accounts.models import CustomUser
from accounts.serializers import UserProfileSerializer
from rest_framework.generics import ListAPIView



class UserSearchView(ListAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        return CustomUser.objects.filter(username__icontains=query)
class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id).order_by('-created_at')

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        post = Post.objects.get(pk=post_id)
        serializer.save(user=self.request.user, post=post)

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        if serializer.instance.user == self.request.user:
            serializer.save()
        else:
            return Response(
                {"detail": "You don't have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN
            )

    def perform_destroy(self, instance):
        if instance.user == self.request.user:
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {"detail": "You don't have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN
            )

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        if request.user in post.likes.all():
            post.likes.remove(request.user)
            return Response({'status': 'unliked'})
        else:
            post.likes.add(request.user)
            return Response({'status': 'liked'})

class LikeCommentView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, comment_id):
        comment = Comment.objects.get(pk=comment_id)
        if request.user in comment.likes.all():
            comment.likes.remove(request.user)
            return Response({'status': 'unliked'})
        else:
            comment.likes.add(request.user)
            return Response({'status': 'liked'})

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = CustomUser.objects.get(pk=user_id)
        if request.user == user_to_follow:
            return Response(
                {'detail': 'You cannot follow yourself.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if request.user in user_to_follow.followers.all():
            user_to_follow.followers.remove(request.user)
            return Response({'status': 'unfollowed'})
        else:
            user_to_follow.followers.add(request.user)
            return Response({'status': 'followed'})