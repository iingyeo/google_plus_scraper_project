from django.contrib import admin
from .models import GooglePlusArticle, GooglePlusArticleSubscriber

# Register your models here.
class GooglePlusArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'date')
    search_fields = ('title', 'link')
admin.site.register(GooglePlusArticle, GooglePlusArticleAdmin)

class GooglePlusArticleSubscriberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created')
    search_fields = ('name', 'email')
admin.site.register(GooglePlusArticleSubscriber, GooglePlusArticleSubscriberAdmin)
