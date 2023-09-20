import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cars.settings')
app = Celery('cars', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'telegram_mailing': {
        'task': 'telegram.tasks.telegram_mailing',
        'schedule': 10
    }
}
