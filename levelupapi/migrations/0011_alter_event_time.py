# Generated by Django 3.2.9 on 2022-01-15 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0010_auto_20211230_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(),
        ),
    ]
