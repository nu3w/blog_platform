from rest_framework import serializers
from .models import Category, Tag, Post, Comment
from django.contrib.auth.models import User

# serializer converts Django models into JSON and vice-versa
class CategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Category
        fields = "__all__"      # include every field in the model
        
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
        
class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Post
        fields = "__all__"
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields ="__all__"
        
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']
        extra_kwargs = {
            'password': {'write_only':True}
        }
        
    def create(self, validated_data):
        user = User.objects.create_user(        # create_user hashes the password
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password']
        )
        return user
    
    