from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from django.core.mail import EmailMessage
from .models import GooglePlusArticle, GooglePlusArticleSubscriber
from datetime import timedelta, date
import subprocess
 
logger = get_task_logger(__name__)
 
# A periodic task that will run every minute (the symbol "*" means every)
@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")))
def execute_spider():
    logger.info("Start scraping task")
    subprocess.Popen(['sh','/Users/taemyung/workspace/github/google_plus_scraper_project/google_plus_scraper/crawl.sh'])
    logger.info("Scraping task finished")

@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")))
def execute_send_mail():
    logger.info("Start sending mail task")
    
    to_list = map(lambda u: u.email, GooglePlusArticleSubscriber.objects.all())

    today = date.today()
    td = timedelta(days=7)
    dateCondition = str(today-td)

    articleList = GooglePlusArticle.objects.all().filter(date__gte=dateCondition)

    contents = """
    <p>Hello, This is Weekly Tech Trends</p>
    <ul>
    """

    for article in articleList:
        contents = contents + '<li><a href="' + article.link + '">' + article.title + '</a></li>'

    contents = contents + '</ul>'

    logger.info('mail contents : ' + contents)

    subject = 'Weekly Tech Trends'
    from_email = 'test@test.com'
    msg = EmailMessage(subject, contents, from_email, to_list)
    msg.content_subtype = "html"
    msg.send()

    logger.info("Sending mail task finished")
