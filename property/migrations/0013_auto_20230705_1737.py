# Generated by Django 3.1 on 2023-07-05 14:37

from django.db import migrations

def del_owners(apps, schema_editor):
    Owners = apps.get_model('property', 'Owner')
    Owners.objects.all().delete()
    print('Delete done.')

def add_owners(apps, schema_editor):
    Flats = apps.get_model('property', 'Flat')
    Owners = apps.get_model('property', 'Owner')
    for flat in Flats.objects.all():
        owner_id = Owners.objects.get_or_create(owner=flat.owner, owner_pure_phone=flat.owner_pure_phone, owners_phonenumber=flat.owners_phonenumber)[0]
        owner_id.owner_flat.add(Flats.objects.get(id=flat.id))
        #owner_id.owner_flat.add(Flats.objects.get(pk=this_object_id))


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20230705_1627'),
    ]

    operations = [
         migrations.RunPython(del_owners),
         migrations.RunPython(add_owners),
    ]