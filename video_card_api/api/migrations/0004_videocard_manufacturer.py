# Generated by Django 2.1.5 on 2019-02-15 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190127_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='videocard',
            name='Manufacturer',
            field=models.CharField(blank=True, max_length=35),
        ),
    ]