# Generated by Django 3.1 on 2023-07-05 13:27

from django.db import migrations

def add_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flats = Flat.objects.all()
    if flats.exists():
        for flat in flats.iterator():
            Owner.objects.get_or_create(owner=flat.owner, owner_pure_phone=flat.owner_pure_phone, owners_phonenumber=flat.owners_phonenumber)[0]


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20230705_1555'),
    ]

    operations = [
         migrations.RunPython(add_owners),
    ]
