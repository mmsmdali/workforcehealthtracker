# -*- coding: utf-8 -*-

#   Licensed to the Apache Software Foundation (ASF) under one
#   or more contributor license agreements.  See the NOTICE file
#   distributed with this work for additional information
#   regarding copyright ownership.  The ASF licenses this file
#   to you under the Apache License, Version 2.0 (the
#   "License"); you may not use this file except in compliance
#   with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing,
#   software distributed under the License is distributed on an
#   "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#   KIND, either express or implied.  See the License for the
#   specific language governing permissions and limitations
#   under the License.
#
#   Built and managed with Open Source Love by BeeHyv Software Solutions Pvt Ltd. Hyderabad
#   www.beehyv.com

# Generated by Django 1.11.17 on 2020-04-24 19:13
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0006_facility_hcw_types'),
    ]

    def insertData(apps, schema_editor):
     CommunicationLanguage = apps.get_model('facility', 'CommunicationLanguage')
     english = CommunicationLanguage(language_name="English")
     hindi = CommunicationLanguage(language_name="Hindi")
     english.save()
     hindi.save()

    operations = [
        migrations.CreateModel(
            name='CommunicationLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(max_length=50, verbose_name='Language name')),
            ],
        ),
        migrations.AlterModelOptions(
            name='facilitytype',
            options={'verbose_name': 'Organization Type'},
        ),
        migrations.AlterField(
            model_name='facility',
            name='facility_name',
            field=models.CharField(max_length=100, verbose_name='Organization Name'),
        ),
        migrations.AlterField(
            model_name='facility',
            name='facility_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.FacilityType', verbose_name='Organization Type'),
        ),
        migrations.AlterField(
            model_name='facilitytype',
            name='facility_type_name',
            field=models.CharField(max_length=50, verbose_name='Organization type name'),
        ),
        migrations.RunPython(insertData),
    ]

