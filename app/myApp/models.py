from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.conf import settings


image_storage = FileSystemStorage(
    # Physical file location ROOT
    location=u'{0}/my_sell/'.format(settings.MEDIA_ROOT),
    # Url for file
    base_url=u'{0}my_sell/'.format(settings.MEDIA_URL),
)


def image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/my_sell/picture/<filename>
    return u'picture/{0}'.format(filename)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.TextField()
    file_field = models.FileField(upload_to=image_directory_path, storage=image_storage)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.author}=> {self.desc}'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

    @property
    def expired_date(self):
        "Returns the expiration date of the File."
        return self.date_posted + datetime.timedelta(days=7)