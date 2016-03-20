from django.conf.urls import url
from . import views


urlpatterns = [
    # subscribe views
    url(r'^$', views.subscribe, name='subscribe'),
    url(r'^subscribe/', views.subscribe, 'subscribe'),
]
