# Generated by Django 4.0.5 on 2022-07-18 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_client_is_client'),
        ('events', '0002_remove_event_support_event_support_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='clients.client'),
        ),
    ]
