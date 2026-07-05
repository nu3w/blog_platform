from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# stores blog categories
class Category(models.Model):
    name = models.CharField(max_length=30, unique=True) 
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
# stores tags that can be assigned to posts
class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name
    
# stores blog posts created by authors
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
# stores comments made on blog posts
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comment by {self.user.username}'