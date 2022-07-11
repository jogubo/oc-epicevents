from rest_framework.serializers import ModelSerializer

from contracts.models import Contract


class ContractSerializer(ModelSerializer):

    class Meta:
        model = Contract
        fields = [
            'id',
            'sales_contact',
            'client',
            'date_created',
            'date_updated',
            'status',
            'amount',
            'payment_due'
        ]
        read_only_fields = ('date_created', 'date_updated',)

    def create(self, validated_data):
        sales_contact = self.context.get('request', None).user

        contract = Contract.objects.create(
            sales_contact=sales_contact,
            client=validated_data['client'],
            status=validated_data['status'],
            amount=validated_data['amount'],
            payment_due=validated_data['payment_due'],
        )
        contract.save()
        return contract

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
