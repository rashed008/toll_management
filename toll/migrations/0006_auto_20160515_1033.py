# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 04:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toll', '0005_accounts'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='Registration_no',
            field=models.CharField(default='Dha-ka-3244', max_length=50),
        ),
        migrations.AddField(
            model_name='tolltransaction',
            name='counter_rate',
            field=models.CharField(default=50, max_length=50),
        ),
    ]