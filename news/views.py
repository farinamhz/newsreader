from django.http import JsonResponse
from django.shortcuts import render
import feedparser

RSS_FEEDS = {'cnn': 'https://www.espn.com/espn/rss/news'}


def get_news(request, publication="cnn"):
    if request.method != 'GET':
        return JsonResponse({"message": "Method was not GET"}, status=400)
        pass
    else:
        feed = feedparser.parse(RSS_FEEDS[publication])
        articles_cnn = feed['entries']

        for article in articles_cnn:
            print("title: \t", article.title_detail.value, "\n")
            print("summary: \t", article.summary_detail.value, "\n")
            print("published date: \t", article.published, "\n")
            print("full news link: \t", article.link, "\n")
            print("******************", "\n")

    return JsonResponse({"message:": "printed in terminal"}, status=200)
