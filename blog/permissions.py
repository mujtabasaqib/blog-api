from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Read allowed to anyone. Write allowed to author only.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only to author
        return obj.author == request.user

