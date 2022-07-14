from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from contracts.models import Contract
from contracts.serializers import ContractSerializer
from contracts.permissions import IsManager, IsSalesman


class ContractViewSet(ModelViewSet):

    serializer_class = ContractSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    permission_classes = (IsAuthenticated, IsManager | IsSalesman)

    def get_queryset(self):
        queryset = Contract.objects.all()
        return queryset
