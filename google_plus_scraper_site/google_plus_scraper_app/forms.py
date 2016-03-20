from django import forms
from .models import GooglePlusArticleSubscriber

class GooglePlusArticleSubscriberForm(forms.ModelForm):
    class Meta:
        model = GooglePlusArticleSubscriber
        fields = ('name', 'email')
