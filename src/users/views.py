from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from users.models import User
from users.serializers import UserSerializer
from users.permissions import ReadOnly


class UserViewSet(ModelViewSet):

    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    permission_classes = (IsAuthenticated, ReadOnly)

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
