# Generated by Django 2.2.24 on 2023-07-13 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_auto_20230712_1049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owner_flat',
            new_name='flat',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owner',
            new_name='full_name',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owner_phone',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owner_phonenumber',
            new_name='phonenumber',
        ),
    ]
