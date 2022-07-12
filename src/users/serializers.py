from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'password',
        ]

        read_only_fields = ('email', 'first_name', 'last_name')

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
        )

        return user

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
