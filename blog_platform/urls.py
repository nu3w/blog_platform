from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TagViewSet, PostViewSet, CommentViewSet, RegisterView
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()

# router automatically generates all CRUD urls
router.register(r'categories', CategoryViewSet)     # r indicates a raw string
router.register(r'tags', TagViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('', include(router.urls)),
]
