# Generated by Django 3.0.5 on 2020-04-22 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ham', '0005_auto_20200422_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='ham',
            name='sex',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='ham',
            name='IMEI',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='ham',
            name='username',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
