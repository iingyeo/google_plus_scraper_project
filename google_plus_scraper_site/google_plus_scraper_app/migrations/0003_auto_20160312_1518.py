# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-12 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('google_plus_scraper_app', '0002_auto_20160312_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='googleplusarticle',
            name='date',
            field=models.CharField(db_index=True, max_length=10),
        ),
    ]
