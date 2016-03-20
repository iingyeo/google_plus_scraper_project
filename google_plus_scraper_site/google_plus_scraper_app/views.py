from django.shortcuts import render
from .forms import GooglePlusArticleSubscriberForm

# Create your views here.
def subscribe(request):
    if request.method == 'POST':
        form = GooglePlusArticleSubscriberForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = GooglePlusArticleSubscriberForm()

    return render(request, 'google_plus_scraper_app/subscribe.html', {'form' : form})
