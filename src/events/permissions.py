from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404

from events.models import Event


class IsManager(BasePermission):

    def has_permission(self, request, view):

        if view.action in ['create', 'list', 'retrieve', 'update', 'destroy']:
            return request.user.groups.filter(name='Manager').exists()
        else:
            return False


class IsSalesman(BasePermission):

    def has_permission(self, request, view):

        if view.action in ['create', 'list', 'retrieve']:
            return request.user.groups.filter(name='Salesman').exists()
        else:
            return False


class IsSupport(BasePermission):

    def has_permission(self, request, view):

        if view.action in ['list', 'retrieve']:
            return request.user.groups.filter(name='Salesman').exists()
        elif view.action in ['update']:
            event = get_object_or_404(Event, pk=view.kwargs['pk'])
            return request.user.is_support_contact(event)
        else:
            return False
