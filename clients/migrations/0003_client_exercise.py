# Generated by Django 3.1.3 on 2020-11-06 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20201105_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='exercise',
            field=models.CharField(default='poco o nada', max_length=20),
            preserve_default=False,
        ),
    ]
