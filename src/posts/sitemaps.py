from django.contrib.sitemaps import Sitemap
from .models import Status


class StatusSitemap(Sitemap):
	changefreq = 'daily'
	priority = 0.9
	
	def items(self):
		return Status.objects.all()
	
	def lastmod(self, obj):
		return obj.timestamp