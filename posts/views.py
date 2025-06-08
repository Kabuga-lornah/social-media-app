from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
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
