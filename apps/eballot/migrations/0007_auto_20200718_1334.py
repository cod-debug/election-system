# Generated by Django 2.2.6 on 2020-07-18 05:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eballot', '0006_auto_20200717_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockholdervote',
            name='result',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stockholdervote',
            name='vote_code',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
    ]