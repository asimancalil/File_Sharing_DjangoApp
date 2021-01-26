import os
from django.conf import settings
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

redis_host = settings.REDIS_HOST
app = Celery('app',
broker='redis://' + settings.REDIS_HOST + ':6379',
backend='redis://' + settings.REDIS_HOST + ':6379',
include=['myApp.tasks']
)
app.conf.update(
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json',
    CELERY_TASK_RESULT_EXPIRES=3600,
    CELERY_TIMEZONE='UTC',
    CELERYBEAT_SCHEDULE={
    'task1': {
    'task': 'myApp.tasks.task1',
    'schedule': crontab(minute=0, hour='*/1'),
    },

    },

    )
app.config_from_object('django.conf:settings')

app.autodiscover_tasks(settings.INSTALLED_APPS)