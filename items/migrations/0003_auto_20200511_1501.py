# Generated by Django 2.2.6 on 2020-05-11 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20200511_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='favorite_users',
            field=models.ManyToManyField(to='favorite.Favorite'),
        ),
    ]
