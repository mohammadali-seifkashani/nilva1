# Generated by Django 3.1.2 on 2020-10-21 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0004_auto_20201020_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='time_created',
        ),
    ]
