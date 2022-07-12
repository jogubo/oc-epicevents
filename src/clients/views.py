from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from clients.models import Client
from clients.seralizers import ClientSerializer


class ClientViewSet(ModelViewSet):

    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name']

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Client.objects.all()
        return queryset
