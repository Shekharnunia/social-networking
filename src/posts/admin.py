from django.contrib import admin

from .models import Status, StatusComment

admin.site.register(Status)
admin.site.register(StatusComment)
