# Generated by Django 3.0.5 on 2020-04-18 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ham',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IMEI', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=10)),
                ('statu', models.BooleanField()),
            ],
        ),
    ]