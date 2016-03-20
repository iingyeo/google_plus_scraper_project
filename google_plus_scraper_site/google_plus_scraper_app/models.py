from __future__ import unicode_literals

from django.db import models

# Create your models here.
class GooglePlusArticle(models.Model):
    title = models.CharField(max_length=1024)
    link = models.CharField(max_length=1024, unique=True)
    date = models.CharField(max_length=10, db_index=True)

    class Meta:
        ordering = ('date',)
    
    def str(self):
        return 'GooglePlusArticle title : {}'.format(self.title)

class GooglePlusArticleSubscriber(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def str(self):
        return 'Subscriber name : {}, email : {}'.format(self.name, self.email)
