# Generated by Django 2.2.6 on 2020-06-04 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20200527_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='adm1',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='adm2',
            field=models.CharField(max_length=30),
        ),
    ]
