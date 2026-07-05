from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Category, Tag, Post, Comment
from .serializers import CategorySerializer, TagSerializer, PostSerializer, CommentSerializer, RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly, IsCommentOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Create your views here.

# allows only admins to modify data while everone can read it
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

# ModelViewSet automatically creates HTTP methods(GET, POST, PUT, PATCH, DELETE)
# handles CRUD operations for blog categories
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()       # retrieve all records from the database
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    
# handles CRUD operations for blog tags
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminOrReadOnly]
    
# handles CRUD operations for blog posts
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    search_fields = ['title','category__name','author__username']
    
    filterset_fields = ['tags']
    
    ordering_fields = ['published_date']
    ordering = ['-published_date']
    
    def perform_create(self, serializer):       # authomatically assigns the logged-in user as author
        serializer.save(author=self.request.user)
    
# handles CRUD operations for blog comments
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    permission_classes = [IsAuthenticatedOrReadOnly, IsCommentOwnerOrReadOnly]
    
    def perform_create(self, serializer):       # authomatically assigns the logged-in user as comment owner
        serializer.save(user=self.request.user)
    
# registers a new user
class RegisterView(generics.CreateAPIView):     # accepts only POST requests for creating new users
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
class LoginView(APIView):       # authenticates a user and returns authentication token
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username = username, password = password)
        if user:
            token,_ = Token.objects.get_or_create(user=user)
            return Response({"token":token.key,"username":username})
        else:
            return Response({"detail":"Invalid username or password"})