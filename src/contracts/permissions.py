from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404

from contracts.models import Contract


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
        elif view.action in ['update']:
            contract = get_object_or_404(Contract, pk=view.kwargs['pk'])
            return request.user.is_sales_contact(contract)
        else:
            return False
