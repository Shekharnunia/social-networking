from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Plan(models.Model):
    MEMBERSHIP_CHOICES = (
        ('Plan1', 'plan1'),
        ('Plan2', 'plan2'),
        ('Plan3', 'plan3')
    )
    slug = models.SlugField()
    plan = models.CharField(choices=MEMBERSHIP_CHOICES, max_length=5, default='Plan1')

    def __str__(self):
        return self.plan


class UserPlan(models.Model):
    plan = models.ForeignKey(Plan,
                             on_delete=models.SET_NULL, null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
