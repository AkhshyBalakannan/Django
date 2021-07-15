from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class comment(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    posted_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
