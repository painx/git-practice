# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-04 04:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(default='A default title', max_length=30)),
                ('Content', models.TextField(default='A default content', max_length=5000)),
                ('Like', models.IntegerField(default=0)),
                ('Pub_date', models.DateTimeField(auto_now_add=True, verbose_name='published date')),
            ],
        ),
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('FM', 'Female'), ('D', 'Default')], default='D', max_length=2)),
                ('Age', models.CharField(choices=[('B', 'Babe'), ('K', 'Kid'), ('S', 'Schoolchild'), ('T', 'Teenage'), ('Y', 'Youth'), ('P', 'Postadolescent'), ('O', 'Old'), ('D', 'Default')], default='D', max_length=2)),
                ('Intro', models.TextField(default='Default intro', help_text='Introduce yourself in 500 words.', max_length=500)),
                ('Admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Commenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Author', models.CharField(max_length=10)),
                ('Content', models.TextField(max_length=500)),
                ('Pub_date', models.DateTimeField(auto_now_add=True, verbose_name='added date')),
                ('Article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tag', models.CharField(max_length=30)),
                ('Article', models.ManyToManyField(to='myblog.Article')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.Blogger'),
        ),
    ]
