# Generated by Django 2.2.6 on 2020-05-16 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direct_messages', '0003_remove_directmessage_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='directmessagecontent',
            name='dm',
        ),
        migrations.AddField(
            model_name='directmessage',
            name='direct_message_contents',
            field=models.ManyToManyField(to='direct_messages.DirectMessageContent'),
        ),
    ]
