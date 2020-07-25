# Generated by Django 2.2.6 on 2020-05-28 05:34

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_auto_20200521_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='item',
            name='radius',
            field=models.IntegerField(default=0),
        ),
    ]
