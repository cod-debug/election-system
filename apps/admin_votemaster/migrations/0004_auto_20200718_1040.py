# Generated by Django 2.2.6 on 2020-07-18 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_votemaster', '0003_attendance_sh_classification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='election_status',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='sh_classification',
        ),
        migrations.RemoveField(
            model_name='nominee',
            name='company_images',
        ),
        migrations.AddField(
            model_name='election',
            name='number_of_nominees',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='election',
            name='number_of_winners',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
