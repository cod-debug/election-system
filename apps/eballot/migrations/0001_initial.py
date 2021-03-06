# Generated by Django 2.2.6 on 2020-07-14 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_votemaster', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EBallotBatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eballot_batch_id', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='EBallotNum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eballot_num', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='StockholderVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sh_id', models.CharField(max_length=250)),
                ('sh_fullname', models.CharField(max_length=250)),
                ('vote_pts', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='EBallot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('election_code', models.CharField(max_length=250)),
                ('sh_fullname', models.CharField(max_length=250)),
                ('eballot_batch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eballot.EBallotBatch')),
                ('eballot_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eballot.EBallotNum')),
                ('sh_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_votemaster.Attendance')),
            ],
        ),
    ]
