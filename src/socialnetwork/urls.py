from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from posts import views
from posts.serializers import StatusViewSet, UserViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'status', StatusViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('plan/', include('plans.urls')),
    path('', include('posts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register, name='register'),
    url(r'^', include(router.urls)),

    url(r'^api-auth/', include('rest_framework.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
