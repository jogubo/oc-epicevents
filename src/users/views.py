from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(ModelViewSet):

    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    # permission_classes = (UserHasPermission,)

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj
