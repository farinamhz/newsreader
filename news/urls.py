from django.urls import path

from . import views

urlpatterns = [
    path('read/fill/', views.fill_db, name='fill-db'),
    path('read/items/', views.get_items, name='get-items'),
    path('read/channel/', views.get_channel, name='get-channel'),
    path('read/items/by-time/', views.get_items_by_time, name='get-items-by-time'),
]
