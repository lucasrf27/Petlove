# Generated by Django 3.0 on 2020-03-15 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_auto_20200313_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pets',
            name='tipo',
            field=models.SmallIntegerField(),
        ),
    ]
