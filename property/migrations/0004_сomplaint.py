# Generated by Django 2.2.24 on 2023-07-05 05:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0003_auto_20230704_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='Сomplaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Текст жалобы')),
                ('complaint_flat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='property.Flat', verbose_name='жалоба на квартиру')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь подавший жалобу')),
            ],
        ),
    ]
