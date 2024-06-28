from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    
    def has_permission(self, request, view):
    #    return bool(request.user and request.user.is_staff)
    #    admin_permission = super().has_permission(request,view)
    #     return request.method == "GET" or admin_permission
        if request.method in permissions.SAFE_METHODS:
            # Check permissions for read-only request
            return True
                
        else:
            return bool(request.user and request.user.is_staff)
                # Check permissions for write request


class ReviewUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
        # Check permissions for read-only request
            return True
        else:
            return obj.review_user == request.user
        # Check permissions for write request
    
           
       
    