from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404

from clients.models import Client


class IsManager(BasePermission):

    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve', 'create', 'update', 'destroy']:
            return request.user.groups.filter(name='Manager').exists()
        else:
            return False


class IsSalesman(BasePermission):

    def has_permission(self, request, view):

        if view.action in ['list', 'retrieve', 'create']:
            return request.user.groups.filter(name='Salesman').exists()
        elif view.action in ['update']:
            client = get_object_or_404(Client, pk=view.kwargs['pk'])
            return request.user.is_sales_contact(client)
        else:
            return False


class IsSupport(BasePermission):

    def has_permission(self, request, view):

        if view.action in ['list', 'retrieve']:
            return request.user.groups.filter(name='Support').exists()
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if obj in Client.objects.filter(events__support_contact=request.user):
            return request.user.groups.filter(name='Support').exists()
