# Generated by Django 3.2.13 on 2022-07-16 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatroom', '0007_alter_channel_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='channels_created', to=settings.AUTH_USER_MODEL),
        ),
    ]