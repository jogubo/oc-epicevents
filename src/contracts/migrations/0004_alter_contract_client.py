# Generated by Django 4.0.5 on 2022-07-18 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_client_is_client'),
        ('contracts', '0003_alter_contract_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='client',
            field=models.ForeignKey(limit_choices_to={'is_client': True}, on_delete=django.db.models.deletion.CASCADE, to='clients.client'),
        ),
    ]
