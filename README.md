# Google Plus Scraper Project

This project is for studying python language.

Scrap google plus article periodically.

Users can register their email to receive scraped google plus article periodically.

[scrapy](http://scrapy.org/) is used to scrap google plus article.

[django](https://www.djangoproject.com/) is used to provide the email subscription form.

[django-celery](http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html) is used to schedule periodical task. 

## Install
```
pip install -r requirements.txt
```

## Run the worker
To run the worker
```
python manage.py celery worker --loglevel=info
```
The worker will run the task whenever the task is queued.

## Run the scheduler
To run the scheduler
```
python manage.py celery beat
```
The scheduler will send the message to the task queue

## Reference

* http://scrapy.org/
* https://www.djangoproject.com/
* http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html
* http://marcela-campo.blogspot.kr/2015/03/scraping-website-using-scrapy-and-django.html
* http://sunshineatnoon.github.io/Use-scrapy-to-scrape-Amazon/
* https://www.caktusgroup.com/blog/2014/06/23/scheduling-tasks-celery/
* http://www.marinamele.com/2014/02/how-to-install-celery-on-django-and.html
