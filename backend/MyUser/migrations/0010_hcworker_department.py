# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-03-27 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyUser', '0009_auto_20200327_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='hcworker',
            name='department',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]