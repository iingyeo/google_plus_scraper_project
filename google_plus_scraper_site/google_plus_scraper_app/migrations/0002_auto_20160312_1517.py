# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-12 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('google_plus_scraper_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='googleplusarticle',
            name='link',
            field=models.CharField(max_length=1024, unique=True),
        ),
    ]
