from django.urls import path
from django.contrib.sitemaps.views import sitemap

from .sitemaps import StatusSitemap
from . import views
from .feeds import LatestStatusFeed

sitemaps = {
	'posts': StatusSitemap,
}


app_name = 'posts'
urlpatterns = [
    path('', views.StatusListView.as_view(), name='list'),
    path('create/', views.CreateStatusView.as_view(), name='create'),
    path('like/', views.StatusLikeView.as_view(), name='like'),
    path('comment/', views.comment, name='comment'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
    	name='django.contrib.sitemaps.views.sitemap'),
    path('feed/', LatestStatusFeed(), name='status_feed'),
]
