from django.db import models
from django.contrib.auth.models import User


class Contract(models.Model):

    sales_contact = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL
    )
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    amount = models.FloatField()
    payment_due = models.DateTimeField()

    def __str__(self):
        return f'{self.payment_due} - {self.client}'
