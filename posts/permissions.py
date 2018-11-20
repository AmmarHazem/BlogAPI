from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_staff


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, req, view, obj):
        if req.method in SAFE_METHODS or obj.author == req.user:
            return True
        return False
