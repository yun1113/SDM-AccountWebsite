# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-02 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20170102_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='item_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]