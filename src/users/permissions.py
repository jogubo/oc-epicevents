from rest_framework.permissions import BasePermission


class ReadOnly(BasePermission):

    def has_permission(self, request, view):

        allowed_actions = ['list', 'retrieve']
        if view.action in allowed_actions:
            return True

        return False
