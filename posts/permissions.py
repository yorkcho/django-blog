from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # GET / HEAD / OPTIONS 允許
        if request.method in SAFE_METHODS:
            return True

        # 非安全方法，只允許作者
        return obj.author == request.user