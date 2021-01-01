from django.http import JsonResponse
from django.shortcuts import render
import feedparser

RSS_FEEDS = {' espn': 'https://www.espn.com/espn/rss/news'}


def get_news(request, publication="espn"):
    if request.method != 'GET':
        return JsonResponse({"message": "Method was not GET"}, status=400)
        pass
    else:
        feed = feedparser.parse(RSS_FEEDS[publication])
        articles_espn = feed['entries']

        for article in articles_espn:
            print(article)
            print("\n")

    return JsonResponse({"message:": "printed in terminal"}, status=200)
