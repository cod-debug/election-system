# Generated by Django 2.2.6 on 2020-07-17 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_votemaster', '0002_auto_20200716_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='sh_classification',
            field=models.CharField(max_length=255, null=True),
        ),
    ]