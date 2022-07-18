from django.db import models
from django.conf import settings


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
        settings.AUTH_USER_MODEL,
        limit_choices_to={'groups__name': 'Salesman'},
        null=True,
        on_delete=models.SET_NULL
    )
    is_client = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.compagny_name}'
