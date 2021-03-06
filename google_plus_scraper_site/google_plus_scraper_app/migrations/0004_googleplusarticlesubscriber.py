# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-20 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('google_plus_scraper_app', '0003_auto_20160312_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='GooglePlusArticleSubscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
