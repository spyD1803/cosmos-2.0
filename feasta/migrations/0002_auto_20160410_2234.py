# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-10 17:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('feasta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='mess',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='feasta.Mess'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='default_mess',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='feasta.Mess'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='redemption',
            name='date',
            field=models.DateField(db_index=True),
        ),
    ]