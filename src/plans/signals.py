from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserPlan


def post_save_user_plan(sender, instance, created, *args, **kwargs):
    if created:
        UserPlan.objects.create(user=instance)


post_save.connect(post_save_user_plan, sender=settings.AUTH_USER_MODEL)
