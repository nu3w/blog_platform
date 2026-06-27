from django.contrib import admin
from .models import Category, Tag, Post, Comment

# Register your models here.

# include models in admin interface
admin.site.register(Category)       
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comment)