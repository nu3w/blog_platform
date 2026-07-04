from django.contrib import admin
from .models import Category, Tag, Post, Comment

# Register your models here.

# include models in admin interface
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    search_fields = ['name']
admin.site.register(Category, CategoryAdmin)     
  
class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']
admin.site.register(Tag,TagAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','author']
    search_fields = ['title','author__username']
admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['post','message','user']
    search_fields = ['post__title']
admin.site.register(Comment, CommentAdmin)