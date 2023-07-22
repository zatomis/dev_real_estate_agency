# Generated by Django 2.2.24 on 2023-07-22 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0022_auto_20230722_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='сomplaint',
            name='complaint',
        ),
        migrations.AddField(
            model_name='сomplaint',
            name='flat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to='property.Flat', verbose_name='жалоба на квартиру'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='flat',
            field=models.ManyToManyField(blank=True, help_text='Квартиры в собственности', related_name='owners', to='property.Flat'),
        ),
    ]
