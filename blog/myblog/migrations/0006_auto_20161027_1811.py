# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 10:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0005_auto_20161027_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogger',
            name='Age',
            field=models.CharField(choices=[('B', 'Babe'), ('K', 'Kid'), ('S', 'Schoolchild'), ('T', 'Teenage'), ('Y', 'Youth'), ('P', 'Postadolescent'), ('O', 'Old')], default=django.utils.timezone.now, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogger',
            name='Gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=django.utils.timezone.now, max_length=2),
            preserve_default=False,
        ),
    ]
