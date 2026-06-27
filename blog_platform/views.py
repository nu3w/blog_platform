from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Tag, Post, Comment
from .serializers import CategorySerializer, TagSerializer, PostSerializer, CommentSerializer

# Create your views here.

# ModelViewSet automatically creates HTTP methods(GET, POST, PUT, PATCH, DELETE)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()       # retrieve all records from the database
    serializer_class = CategorySerializer
    
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer