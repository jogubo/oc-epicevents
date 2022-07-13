from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404

from clients.models import Client


class IsSalesContactOrReadOnly(BasePermission):

    def has_permission(self, request, view):

        allowed_actions = ['create', 'list']
        if view.action in allowed_actions:
            return True

        allowed_actions = ['retrieve', 'update', 'destroy']
        if view.action in allowed_actions:
            client = get_object_or_404(Client, pk=view.kwargs['pk'])
            return request.user.is_sales_contact(client)

        return False


class IsManagerOrReadOnly(BasePermission):

    def has_permission(self, request, view):

        allowed_actions = ['create', 'list']
        if view.action in allowed_actions:
            return True

        allowed_actions = ['retrieve', 'update', 'destroy']
        if view.action in allowed_actions:
            return request.user.groups.filter(name='Manager').exists()

        return False


class IsSalesman(BasePermission):

    def has_permission(self, request, view):

        allowed_actions = ['create', 'list', 'retrieve', 'update', 'destroy']
        if view.action in allowed_actions:
            return request.user.groups.filter(name='Salesman').exists()

        return False
