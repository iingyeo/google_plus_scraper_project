from django.contrib import admin
from .models import GooglePlusArticle

# Register your models here.
class GooglePlusArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'date')
admin.site.register(GooglePlusArticle, GooglePlusArticleAdmin)