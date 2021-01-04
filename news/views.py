from django.http import JsonResponse
import email.utils as x
from datetime import datetime
import feedparser
from rest_framework.decorators import api_view
from .models import Item, Channel
from rest_framework.pagination import PageNumberPagination
from .serializers import ItemReadSerializer, ChannelReadSerializer


@api_view(['GET', ])
def fill_db(request, publication="cnn"):
    RSS_FEEDS = {'cnn': 'http://rss.cnn.com/rss/edition.rss'}
    feed = feedparser.parse(RSS_FEEDS[publication])
    articles_cnn = feed['entries']
    id_list = []

    # adding news Item
    article_base_channel = feed.feed
    ch_subtitle_detail = article_base_channel.subtitle_detail.value
    ch_title = article_base_channel.title_detail.value
    ch_base_link = article_base_channel.title_detail.base
    ch_image = article_base_channel.image.href
    ch_language = article_base_channel.language
    ch_rights_detail = article_base_channel.rights_detail.value
    ch_generator = article_base_channel.generator
    ch_updated = article_base_channel.updated

    channel = Channel.objects.create(subtitle_detail=ch_subtitle_detail, base_link=ch_base_link,
                                     title=ch_title, image=ch_image, language=ch_language,
                                     rights_detail=ch_rights_detail, generator=ch_generator,
                                     updated=ch_updated)
    channel.save()
    id_list.append(channel.id)

    # adding news Item
    for article in articles_cnn:
        published_date = title = summary = link = image_url = ''
        if hasattr(article, 'published'):
            published_date = str(datetime.fromtimestamp(x.mktime_tz(x.parsedate_tz(article.published))))
        else:
            continue
        if hasattr(article, 'title_detail'):
            title = article.title_detail.value
        if hasattr(article, 'summary_detail'):
            summary = article.summary_detail.value
        if hasattr(article, 'link'):
            link = article.link
        if hasattr(article, 'media_content'):
            image_url = article.media_content[0]["url"]
        try:
            item = Item.objects.create(published_date=published_date, title=title, summary=summary,
                                       link=link, image_url=image_url)
            item.save()
            id_list.append(item.id)
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=400)
    return JsonResponse({"id_list": id_list}, status=201)


# get all news with filter on numbers
@api_view(['GET', ])
def get_items(request):
    items = Item.objects.all()
    ordered = sorted(items, key=lambda item: datetime.strptime(item.published_date, '%Y-%m-%d %H:%M:%S'), reverse=True)
    # ordered = sorted(items, key=operator.attrgetter('last_name'), reverse=True)
    paginator = PageNumberPagination()
    paginator.page_size = request.data['size']
    result_page = paginator.paginate_queryset(ordered, request)
    item_ser = ItemReadSerializer(result_page, many=True)
    return paginator.get_paginated_response(item_ser.data)


# get channel
@api_view(['GET', ])
def get_channel(request):
    chan = Channel.objects.all()
    paginator = PageNumberPagination()
    paginator.page_size = 1
    result_page = paginator.paginate_queryset(chan, request)
    chan_ser = ChannelReadSerializer(result_page, many=True)
    return paginator.get_paginated_response(chan_ser.data)


@api_view(['GET', ])
def get_items_by_time(request):
    # items = Item.objects.all()
    from_date = datetime.strptime(request.data['from_date'], '%Y-%m-%d %H:%M:%S')
    to_date = datetime.strptime(request.data['to_date'], '%Y-%m-%d %H:%M:%S')
    items = Item.objects.filter(published_date__range=(from_date, to_date))
    ordered = sorted(items, key=lambda item: datetime.strptime(item.published_date, '%Y-%m-%d %H:%M:%S'),
                      reverse=True)
    paginator = PageNumberPagination()
    paginator.page_size = request.data['size']
    result_page = paginator.paginate_queryset(ordered, request)
    item_ser = ItemReadSerializer(result_page, many=True)
    return paginator.get_paginated_response(item_ser.data)
