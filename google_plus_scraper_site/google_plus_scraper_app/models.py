from __future__ import unicode_literals

from django.db import models

# Create your models here.
class GooglePlusArticle(models.Model):
    title = models.CharField(max_length=1024)
    link = models.CharField(max_length=1024, unique=True)
    date = models.CharField(max_length=10, db_index=True)
