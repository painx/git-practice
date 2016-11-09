# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-09 02:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20161108_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogger',
            name='Age',
            field=models.CharField(choices=[('B', '\u7ae5\u5e74'), ('K', '\u5e7c\u5e74'), ('S', '\u5c11\u5e74'), ('T', '\u9752\u5e74'), ('Y', '\u58ee\u5e74'), ('P', '\u4e2d\u5e74'), ('O', '\u8001\u725b')], default='B', max_length=2, verbose_name='\u5e74\u7eaa'),
        ),
        migrations.AlterField(
            model_name='blogger',
            name='Gender',
            field=models.CharField(choices=[('M', '\u7537'), ('FM', '\u5973')], default='M', max_length=2, verbose_name='\u6027\u522b'),
        ),
    ]
