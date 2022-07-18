from django.db import models
from django.conf import settings


class Contract(models.Model):

    sales_contact = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        limit_choices_to={'groups__name': 'Salesman'},
        null=True,
        on_delete=models.SET_NULL
    )
    client = models.ForeignKey(
        'clients.Client',
        on_delete=models.CASCADE,
        limit_choices_to={'is_client': True},
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False, verbose_name='Signed')
    amount = models.FloatField()
    payment_due = models.DateTimeField()

    def __str__(self):
        return f'{self.payment_due} - {self.client}'
