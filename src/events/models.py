from django.db import models
from django.contrib.auth.models import User

from clients.models import Client


class Event(models.Model):

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL
    )
    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    note = models.TextField()

    def __str__(self):
        return f'{self.event_date} - {self.client}'
