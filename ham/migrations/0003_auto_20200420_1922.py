# Generated by Django 3.0.5 on 2020-04-20 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ham', '0002_auto_20200420_1911'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ham',
            old_name='name',
            new_name='username',
        ),
    ]
