# Generated by Django 2.2.3 on 2020-07-14 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20200606_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='images/user_icon.png', null=True, upload_to='images/'),
        ),
    ]
