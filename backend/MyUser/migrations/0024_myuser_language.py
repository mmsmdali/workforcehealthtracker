# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-04-25 07:55
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0008_facility_language'),
        ('MyUser', '0023_hcworker_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='language',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='facility.CommunicationLanguage'),
            preserve_default=False,
        ),
    ]