from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from events.models import Event
from events.serializers import EventSerializer

from users.permissions import UserHasPermission


class EventViewSet(ModelViewSet):

    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    permission_classes = (UserHasPermission,)

    def get_queryset(self):
        queryset = Event.objects.all()
        return queryset
