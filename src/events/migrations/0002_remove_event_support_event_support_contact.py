# Generated by Django 4.0.5 on 2022-07-14 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='support',
        ),
        migrations.AddField(
            model_name='event',
            name='support_contact',
            field=models.ForeignKey(limit_choices_to={'groups__name': 'Support'}, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
