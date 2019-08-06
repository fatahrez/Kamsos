# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-06 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vet',
            name='county',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='vet',
            name='qualifications',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='vet',
            name='sub_county',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='vet',
            name='telephone_number',
            field=models.CharField(max_length=13, null=True, unique=True),
        ),
    ]
