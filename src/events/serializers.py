from rest_framework.serializers import ModelSerializer

from events.models import Event


class EventSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = [
            'id',
            'client',
            'date_created',
            'date_updated',
            'support_contact',
            'attendees',
            'event_date',
            'note',
        ]
        read_only_fields = ('date_created', 'date_updated')

    def create(self, validated_data):
        event = Event.objects.create(
            client=validated_data['client'],
            support=validated_data['support_contact'],
            attendees=validated_data['attendees'],
            event_date=validated_data['event_date'],
            note=validated_data['note'],
        )
        event.save()

        return event

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
