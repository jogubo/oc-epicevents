from django.db import models
from django.conf import settings

from clients.models import Client


class Event(models.Model):

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='events'
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        limit_choices_to={'groups__name': 'Support'},
        null=True,
        on_delete=models.SET_NULL
    )
    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    note = models.TextField()

    def __str__(self):
        return f'{self.event_date} - {self.client}'
