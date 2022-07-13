from rest_framework.permissions import BasePermission


class IsSalesman(BasePermission):

    def has_permission(self, request, view):

        allowed_actions = ['create', 'list', 'retrieve', 'update', 'destroy']
        if view.action in allowed_actions:
            return request.user.groups.filter(name='Salesman').exists()
            return True

        else:
            return False
