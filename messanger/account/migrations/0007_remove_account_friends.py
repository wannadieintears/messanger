# Generated by Django 4.2.6 on 2023-10-17 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_account_friends'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='friends',
        ),
    ]