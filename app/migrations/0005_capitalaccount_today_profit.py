# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-19 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_capitalaccount_initial_money'),
    ]

    operations = [
        migrations.AddField(
            model_name='capitalaccount',
            name='today_profit',
            field=models.FloatField(default=0, help_text='当天收益'),
        ),
    ]