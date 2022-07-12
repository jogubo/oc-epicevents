from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from clients.models import Client
from clients.seralizers import ClientSerializer


class ClientViewSet(ModelViewSet):

    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Client.objects.all()
        return queryset
