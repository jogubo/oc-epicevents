from django.db import models
from django.contrib.auth.models import User

from contracts.models import Contract


class Client(models.Model):

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    compagny_name = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return f'{self.compagny_name}'

    def is_client(self):
        contracts = Contract.objects.filter(client=self, status=False)
        return True if contracts else False
