# Generated by Django 3.0 on 2020-03-21 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0007_auto_20200321_1222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='user1',
            new_name='user',
        ),
    ]
