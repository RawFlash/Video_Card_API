# Generated by Django 2.1.5 on 2019-01-27 04:04

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_conv_videocard'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='videocard',
            managers=[
                ('objects1', django.db.models.manager.Manager()),
            ],
        ),
    ]
