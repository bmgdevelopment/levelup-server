# Generated by Django 3.2.9 on 2021-12-15 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0006_event_attendees'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='attendees',
        ),
    ]