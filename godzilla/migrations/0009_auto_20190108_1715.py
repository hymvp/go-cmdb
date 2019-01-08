# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-08 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('godzilla', '0008_auto_20190108_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordlogtable',
            name='logtime',
            field=models.DateTimeField(default='2019-01-08 17:14:58'),
        ),
        migrations.AlterField(
            model_name='redishost',
            name='admin_addr',
            field=models.GenericIPAddressField(null=True),
        ),
    ]