# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-23 01:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geofence', '0002_auto_20171020_0925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='child_name',
        ),
        migrations.AddField(
            model_name='history',
            name='child_geotype',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='history',
            name='child_response',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='history',
            name='cpn',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='geofence.Company'),
        ),
        migrations.AddField(
            model_name='history',
            name='response',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='history',
            name='event_duration',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='history',
            name='geo_time',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='history',
            name='geotype',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='cpn',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='geofence.Company'),
        ),
    ]
