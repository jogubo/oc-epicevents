from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from clients.models import Client
from clients.serializers import ClientSerializer
from clients.permissions import IsManager, IsSalesman, IsSupport


class ClientViewSet(ModelViewSet):

    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    permission_classes = (IsAuthenticated, IsManager | IsSalesman | IsSupport)

    def get_queryset(self):
        if self.request.user.groups.filter(name='Support').exists():
            queryset = Client.objects.filter(
                events__support_contact=self.request.user
            ).distinct()
        else:
            queryset = Client.objects.all()
        return queryset
