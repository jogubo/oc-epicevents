from rest_framework.permissions import BasePermission


class IsVendor(BasePermission):

    def has_permission(self, request, view):

        allowed_actions = ['create', 'list', 'retrieve', 'update', 'destroy']
        if view.action in allowed_actions:
            return request.user.groups.filter(name='Vendor').exists()
            return True

        else:
            return False
