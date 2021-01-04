from django.http import JsonResponse
import email.utils as x
from datetime import datetime
import feedparser
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

RSS_FEEDS = {'cnn': 'http://rss.cnn.com/rss/edition.rss'}


@api_view(['GET', ])
def get_items(request, publication="cnn"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    articles_cnn = feed['entries']

    output_list = []

    for article in articles_cnn:
        context = {}
        if hasattr(article, 'published'):
            # print(datetime.fromtimestamp(x.mktime_tz(x.parsedate_tz(article.published))))
            context["published_date"] = str(datetime.fromtimestamp(x.mktime_tz(x.parsedate_tz(article.published))))
        else:
            continue
        if hasattr(article, 'title_detail'):
            context["title"] = article.title_detail.value
        if hasattr(article, 'summary_detail'):
            context["summary"] = article.summary_detail.value
        if hasattr(article, 'link'):
            context["link"] = article.link
        if hasattr(article, 'media_content'):
            context["image_url"] = article.media_content[0]["url"]
        output_list.append(context)

    output_list.sort(key=lambda item: datetime.strptime(item['published_date'], '%Y-%m-%d %H:%M:%S'), reverse=True)
    # for a in output_list:
    #     print(a, "\n")

    return JsonResponse(output_list, status=200, safe=False)


@api_view(['GET', ])
def get_channel(request, publication="cnn"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    article_base_channel = feed.feed
    article_channel_context = {"subtitle_detail": article_base_channel.subtitle_detail.value,
                               "title": article_base_channel.title_detail.value,
                               "base_link": article_base_channel.title_detail.base,
                               "image": article_base_channel.image.href,
                               "language": article_base_channel.language,
                               "rights_detail": article_base_channel.rights_detail.value,
                               "generator": article_base_channel.generator,
                               "updated": article_base_channel.updated,
                               }

    # print(article_channel_context)

    return JsonResponse(article_channel_context, status=200, safe=False)
