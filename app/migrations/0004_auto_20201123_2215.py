# Generated by Django 3.1.3 on 2020-11-24 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201123_1817'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restaurant',
            options={'permissions': (('verified_restaurant', 'Verified restaurant account'),)},
        ),
    ]
