# Generated by Django 3.0 on 2020-03-13 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_auto_20200313_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pets',
            name='tipo',
            field=models.SmallIntegerField(choices=[(1, 'CACHORRO'), (3, 'OUTRO')]),
        ),
    ]
