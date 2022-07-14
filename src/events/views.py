from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from events.models import Event
from events.serializers import EventSerializer
from events.permissions import IsManager, IsSalesman, IsSupport


class EventViewSet(ModelViewSet):

    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    permission_classes = (IsAuthenticated, IsManager | IsSalesman | IsSupport)

    def get_queryset(self):
        queryset = Event.objects.all()
        return queryset
