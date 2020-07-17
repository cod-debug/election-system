# Generated by Django 2.2.6 on 2020-07-17 04:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eballot', '0005_merge_20200716_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('election_code', models.CharField(max_length=250)),
                ('date_last_updated', models.DateTimeField(auto_now=True)),
                ('eballot_num', models.CharField(max_length=250)),
                ('vote_allocated', models.CharField(max_length=250)),
                ('nominee_fullname', models.CharField(max_length=250)),
                ('vote_pts', models.IntegerField(default=0)),
                ('result', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='eballot',
            name='alert',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='eballot',
            name='election_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='eballot',
            name='sh_classification',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
    ]
