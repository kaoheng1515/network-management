# Generated by Django 4.2.11 on 2025-05-27 13:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('network', '0004_alter_networkdevice_building_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='networkdevice',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_devices', to=settings.AUTH_USER_MODEL),
        ),
    ]
