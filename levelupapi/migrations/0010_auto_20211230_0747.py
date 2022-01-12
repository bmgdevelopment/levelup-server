# Generated by Django 3.2.9 on 2021-12-30 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0009_auto_20211222_0305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='location',
        ),
        migrations.RemoveField(
            model_name='event',
            name='title',
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.CharField(default='Game info here', max_length=150),
        ),
    ]