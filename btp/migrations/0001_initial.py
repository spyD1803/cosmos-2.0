# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-30 06:26
from __future__ import unicode_literals

import btp.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BTPEvalPanel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('members', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BTPEvalSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupno', models.PositiveIntegerField(default=0)),
                ('projectgroups', models.TextField()),
                ('panel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='btp.BTPEvalPanel')),
            ],
        ),
        migrations.CreateModel(
            name='BTPMarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('panelmarks', models.PositiveIntegerField(default=0)),
                ('panelstrength', models.PositiveIntegerField(default=0)),
                ('paneltime', models.DateTimeField(auto_now=True)),
                ('externalmarks', models.PositiveIntegerField(default=0)),
                ('externaltime', models.DateTimeField(auto_now=True)),
                ('btpcmarks', models.PositiveIntegerField(default=0)),
                ('btpctime', models.DateTimeField(auto_now=True)),
                ('supervisormarks', models.PositiveIntegerField(default=0)),
                ('supervisortime', models.DateTimeField(auto_now=True)),
                ('bonusmarks', models.PositiveIntegerField(default=0)),
                ('bonusmarkstime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BTPProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=8)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(default=b'NA')),
                ('supervisor', models.TextField()),
                ('isfileuploaded', models.BooleanField(default=False)),
                ('isexternal', models.BooleanField(default=False)),
                ('fileuploaded', models.FileField(blank=True, null=True, upload_to=b'')),
                ('display', models.BooleanField(default=True)),
                ('postedby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BTPProjectGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('students', models.TextField()),
                ('faculty', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='btp.BTPProject')),
            ],
        ),
        migrations.CreateModel(
            name='BTPSetWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evalday', models.DateField(default=datetime.datetime(2016, 8, 30, 6, 26, 57, 437843, tzinfo=utc))),
                ('starttime', models.DateField()),
                ('endtime', models.DateField()),
                ('submitdeadline', models.DateTimeField()),
                ('sets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='btp.BTPEvalSet')),
            ],
        ),
        migrations.CreateModel(
            name='BTPStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=5)),
                ('rollno', models.CharField(max_length=15)),
                ('btpproject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='btp.BTPProject')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BTPSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_at', models.DateTimeField(auto_now=True)),
                ('fileuploaded', models.FileField(upload_to=btp.models.content_file_name)),
                ('projectgroup', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='btp.BTPProjectGroup')),
                ('submitted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='btp.BTPSetWeek')),
            ],
        ),
        migrations.CreateModel(
            name='BTPWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekno', models.PositiveIntegerField(default=0)),
                ('starttime', models.DateTimeField()),
                ('endtime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=25)),
                ('fileupload', models.FileField(upload_to=b'/static/btp/files/')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('sem', models.SmallIntegerField()),
                ('batch', models.CharField(choices=[(b'UG1', b'UG1'), (b'UG2', b'UG2'), (b'UG3', b'UG3'), (b'UG4', b'UG4')], max_length=5)),
                ('start', models.DateField()),
                ('end', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='btpweek',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='btp.Semester'),
        ),
        migrations.AddField(
            model_name='btpsetweek',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='btp.BTPWeek'),
        ),
        migrations.AddField(
            model_name='btpmarks',
            name='btpweek',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='btp.BTPWeek'),
        ),
        migrations.AddField(
            model_name='btpmarks',
            name='projectgroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='btp.BTPProjectGroup'),
        ),
        migrations.AddField(
            model_name='btpmarks',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='btp.Semester'),
        ),
    ]