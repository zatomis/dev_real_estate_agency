# Generated by Django 3.1 on 2023-07-05 11:17

from django.db import migrations
import phonenumbers

def correct_phone_number(apps, schema_editor):
    Flats = apps.get_model('property', 'Flat')
    for flat in Flats.objects.all():
        valid_phone_number = str(phonenumbers.parse(flat.owner_pure_phone, 'RU')).split(' ')[5]
        if valid_phone_number:
            flat.owners_phonenumber = f"+7{valid_phone_number}"
            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20230705_1347'),
    ]

    operations = [
        migrations.RunPython(correct_phone_number),
    ]

