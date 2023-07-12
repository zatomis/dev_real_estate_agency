# Generated by Django 2.2.24 on 2023-07-04 12:59

from django.db import migrations

def set_property_new_building(apps, schema_editor):
    Flats = apps.get_model('property', 'Flat')
    for flat in Flats.objects.all():
        if flat.construction_year >= 2015:
            flat.new_building = True
            flat.save()
        else:
            flat.new_building = False
            flat.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20230704_1513'),
    ]

    operations = [
	    migrations.RunPython(set_property_new_building),
    ]