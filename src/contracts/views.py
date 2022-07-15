from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from contracts.models import Contract
from contracts.serializers import ContractSerializer

from users.permissions import UserHasPermission


class ContractViewSet(ModelViewSet):

    serializer_class = ContractSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    permission_classes = (UserHasPermission,)

    def get_queryset(self):
        queryset = Contract.objects.all()
        return queryset
