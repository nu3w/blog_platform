from rest_framework.permissions import BasePermission, SAFE_METHODS

# allows only the post author to edit or delete a post
class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:      # only read data(GET, HEAD, OPTIONS)
            return True
        return obj.author == request.user
    
# allows only the comment owner to edit or delete a comment
class IsCommentOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user