from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.TextField()
    file_field = models.FileField(upload_to='uploads/')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.author}=> {self.desc}'