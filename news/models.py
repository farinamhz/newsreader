from django.db import models


# Create your models here.


class Item(models.Model):
    title = models.TextField()
    summary = models.TextField()
    link = models.TextField()
    image_url = models.TextField()
    published_date = models.TextField()

    def __str__(self):
        return self.title


class Index(models.Model):
    # Key Word
    kw = models.TextField(unique=True, null=False)
    # News
    items = models.ManyToManyField(Item)

    def __str__(self):
        return self.kw


class Channel(models.Model):
    subtitle_detail = models.TextField()
    title = models.TextField()
    base_link = models.TextField()
    image = models.TextField()
    language = models.TextField()
    rights_detail = models.TextField()
    generator = models.TextField()
    updated = models.TextField()
