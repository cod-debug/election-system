# Generated by Django 2.2.6 on 2020-07-18 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_newstockholder', '0003_stockholder_eballot_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockholder',
            name='eballot_no',
        ),
    ]
