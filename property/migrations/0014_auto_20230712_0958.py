# Generated by Django 2.2.24 on 2023-07-12 06:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20230705_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_posts', to=settings.AUTH_USER_MODEL, verbose_name='лайк'),
        ),
    ]
