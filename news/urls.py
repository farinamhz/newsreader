from django.urls import path

from . import views

urlpatterns = [
    # products urls
    path('read/', views.get_news, name='product_insert'),
]
