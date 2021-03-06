# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-30 07:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geofence', '0003_auto_20171023_0156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='child',
            old_name='pos_lat',
            new_name='enter_lat',
        ),
        migrations.RenameField(
            model_name='child',
            old_name='pos_long',
            new_name='enter_long',
        ),
        migrations.RenameField(
            model_name='geofence',
            old_name='pos_lat',
            new_name='enter_lat',
        ),
        migrations.RenameField(
            model_name='geofence',
            old_name='pos_long',
            new_name='enter_long',
        ),
        migrations.AddField(
            model_name='child',
            name='exit_lat',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='child',
            name='exit_long',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='geofence',
            name='exit_lat',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='geofence',
            name='exit_long',
            field=models.CharField(default='', max_length=200),
        ),
    ]
