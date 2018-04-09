from django.shortcuts import render
from rest_framework import generics

from wall.models import Post
from .serializers import PostSerializer

class PostView(generics.ListCreateAPIView):
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer 
