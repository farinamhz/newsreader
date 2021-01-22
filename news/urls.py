from django.urls import path

from . import views

urlpatterns = [
    path('read/fill/', views.fill_db, name='fill-db'),
    path('read/index_news/', views.index_db, name='fill-db'),
    path('read/items/', views.get_items, name='get-items'),
    path('read/channel/', views.get_channel, name='get-channel'),
    path('read/items/by-filter/', views.get_items_by_filter, name='get-items--by-filter'),
    path('read/items/search/', views.search_on_items, name='search-on-items'),
]
