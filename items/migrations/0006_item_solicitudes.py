# Generated by Django 2.2.6 on 2020-05-14 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0002_remove_solicitud_item'),
        ('items', '0005_item_item_contacts'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='solicitudes',
            field=models.ManyToManyField(to='solicitudes.Solicitud'),
        ),
    ]