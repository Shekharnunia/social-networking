from django.conf import settings
from django.db import models
from django.utils.text import slugify


plans = (
    ('Plan1', 'plan1'),
    ('Plan2', 'plan2'),
    ('Plan3', 'plan3'),
)


class Plan(models.Model):
    slug = models.SlugField()
    plan = models.CharField(choices=plans, max_length=50)


class UserPlan(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, default='Plan1')
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
