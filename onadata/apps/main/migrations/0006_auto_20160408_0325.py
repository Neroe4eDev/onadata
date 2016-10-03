# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-08 07:25
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20160404_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audit',
            name='json',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='metadata',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
    ]
