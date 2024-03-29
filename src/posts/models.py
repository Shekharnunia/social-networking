from django.conf import settings
from django.db import models
from django.urls import reverse

from plans.models import Plan


class Status(models.Model):
    content = models.TextField()
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='status_like')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('posts:list')


class StatusComment(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    comment = models.CharField(max_length=250)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
