# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-06 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_auto_20160503_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basics',
            name='address1',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='basics',
            name='city',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='basics',
            name='postalCode',
            field=models.CharField(blank=True, max_length=255, verbose_name='post code'),
        ),
        migrations.AlterField(
            model_name='basics',
            name='region',
            field=models.CharField(blank=True, max_length=255, verbose_name='State/Province'),
        ),
    ]