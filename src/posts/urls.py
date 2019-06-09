from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.StatusListView.as_view(), name='list'),
    path('create/', views.CreateStatusView.as_view(), name='create'),
    path('like/', views.StatusLikeView.as_view(), name='like'),
    path('comment/', views.comment, name='comment'),
]

