from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords

from .models import Status

class LatestStatusFeed(Feed):
    title = 'My Status'
    link = '/status/'
    description = 'New status of my website.'

    def items(self):
        return Status.objects.all()[:10]

    def item_title(self, item):
        return item.content

    def item_description(self, item):
        return None