# Generated by Django 2.2.6 on 2020-07-18 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_votemaster', '0005_attendance_eballot_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='eballot_no',
        ),
        migrations.AddField(
            model_name='attendance',
            name='election_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='attendance',
            name='sh_classification',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='sh_proxy_status',
            field=models.BooleanField(default=False),
        ),
    ]
