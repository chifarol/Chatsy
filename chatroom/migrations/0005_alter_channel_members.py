# Generated by Django 3.2.13 on 2022-07-16 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0004_alter_channel_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='members',
            field=models.ManyToManyField(blank=True, null=True, related_name='channels', to='chatroom.Member'),
        ),
    ]
