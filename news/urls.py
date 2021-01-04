from django.urls import path

from . import views

urlpatterns = [
    # products urls
    path('read/items', views.get_items, name='get-items'),
    path('read/channel', views.get_channel, name='get-channel'),
]
