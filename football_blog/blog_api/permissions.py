from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow GET, HEAD, OPTIONS requests to all users
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Check if the user is the owner of the object
        return obj.user == request.user