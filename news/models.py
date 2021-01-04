from django.db import models

# Create your models here.


class Item(models.Model):
    title = models.TextField(unique=True)
    summary = models.TextField()
    link = models.TextField()
    image_url = models.TextField()
    published_date = models.TextField()


class Channel(models.Model):
    subtitle_detail = models.TextField()
    title = models.TextField()
    base_link = models.TextField(unique=True)
    image = models.TextField()
    language = models.TextField()
    rights_detail = models.TextField()
    generator = models.TextField()
    updated = models.TextField()