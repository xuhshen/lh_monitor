# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-19 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='capitalaccount',
            name='product',
            field=models.CharField(default='', help_text='产品名字', max_length=200),
            preserve_default=False,
        ),
    ]
