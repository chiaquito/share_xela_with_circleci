# Generated by Django 2.2.6 on 2020-06-04 13:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0009_auto_20200527_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='categories.Category'),
        ),
        migrations.AlterField(
            model_name='item',
            name='direct_message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='direct_messages.DirectMessage'),
        ),
        migrations.AlterField(
            model_name='item',
            name='favorite_users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='item',
            name='image1',
            field=models.ImageField(blank=True, default='images/default_item.jpeg', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_contacts',
            field=models.ManyToManyField(blank=True, to='item_contacts.ItemContact'),
        ),
        migrations.AlterField(
            model_name='item',
            name='solicitudes',
            field=models.ManyToManyField(blank=True, to='solicitudes.Solicitud'),
        ),
    ]