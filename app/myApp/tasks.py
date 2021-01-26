from celery import shared_task
from .models import Post
from datetime import datetime
import pytz


@shared_task
def task1():
    objs = Post.objects.all()
    now = datetime.now()
    timezone = pytz.timezone('UTC')
    now_localize = timezone.localize(now)

    for obj in objs:
        if obj.expired_date < now_localize :
            obj.delete()
    return "completed deleting file at {}".format(timezone.now())