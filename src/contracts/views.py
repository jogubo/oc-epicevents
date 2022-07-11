from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from contracts.models import Contract
from contracts.seralizers import ContractSerializer


class ContractViewSet(ModelViewSet):

    serializer_class = ContractSerializer

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Contract.objects.all()
        return queryset
