from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
import subprocess
 
logger = get_task_logger(__name__)
 
# A periodic task that will run every minute (the symbol "*" means every)
@periodic_task(run_every=(crontab(hour="*", minute="0", day_of_week="*")))
def execute_spider():
    logger.info("Start scraping task")
    subprocess.Popen(['sh','/Users/taemyung/workspace/github/google_plus_scraper_project/google_plus_scraper/crawl.sh'])
    logger.info("Scraping task finished")
