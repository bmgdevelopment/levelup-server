# Generated by Django 3.2.9 on 2021-12-14 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0003_auto_20211214_0255'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(related_name='myevents', to='levelupapi.Gamer'),
        ),
    ]
