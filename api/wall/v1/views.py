from django.shortcuts import render
from rest_framework import generics, permissions

from wall.models import Post
from .serializers import PostSerializer

class PostView(generics.ListCreateAPIView):
    """
    get:
    Returns a list of Posts

    post:
    Create a Post resource
    """
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
