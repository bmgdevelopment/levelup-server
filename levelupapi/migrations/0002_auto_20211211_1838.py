# Generated by Django 3.2.9 on 2021-12-11 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=55)),
            ],
        ),
        migrations.RemoveField(
            model_name='game',
            name='type',
        ),
        migrations.AddField(
            model_name='game',
            name='gametype',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='levelupapi.gametype'),
            preserve_default=False,
        ),
    ]