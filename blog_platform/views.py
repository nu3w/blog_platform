from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Category, Tag, Post, Comment
from .serializers import CategorySerializer, TagSerializer, PostSerializer, CommentSerializer, RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly, IsCommentOwnerOrReadOnly


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
    
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    permission_classes = [IsAuthenticatedOrReadOnly, IsCommentOwnerOrReadOnly]
    
class RegisterView(generics.CreateAPIView):     # accepts only POST requests for creating new users
    queryset = User.objects.all()
    serializer_class = RegisterSerializer