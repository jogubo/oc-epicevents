from rest_framework.serializers import ModelSerializer

from clients.models import Client


class ClientSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'mobile',
            'compagny_name',
            'date_created',
            'date_updated',
            'sales_contact',
            'is_client'
        ]
        read_only_fields = ('date_created', 'date_updated',)

    def create(self, validated_data):
        client = Client.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            mobile=validated_data['mobile'],
            compagny_name=validated_data['compagny_name'],
            sales_contact=validated_data['sales_contact'],
        )
        client.save()

        return client

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
