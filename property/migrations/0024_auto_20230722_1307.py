# Generated by Django 2.2.24 on 2023-07-22 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0023_auto_20230722_1304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='flat',
            new_name='flats',
        ),
    ]
