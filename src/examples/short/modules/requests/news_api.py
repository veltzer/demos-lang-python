"""
news_api.py
"""

import sys
import requests
import pyapikey

key = pyapikey.get_key("newsapi.org")

do_headlines = False
do_everything = True

if do_headlines:
    url = f"http://newsapi.org/v2/top-headlines?country=us&apiKey={key}"
    r = requests.get(url, timeout=5)
    r.raise_for_status()
    obj = r.json()

    articles = obj["articles"]
    for i, article in enumerate(articles):
        title = article["title"]
        print(f"{i}: {title}")


if do_everything:
    param_q = "qInTitle=corona&"
    mydict = {
        "qInTitle": sys.argv[1],
        "pageSize": 20,
        "page": 1,
        "apiKey": key,
    }
    url = "http://newsapi.org/v2/everything"
    r = requests.get(url, params=mydict, timeout=5)
    r.raise_for_status()
    obj = r.json()

    articles = obj["articles"]
    for i, article in enumerate(articles):
        title = article["title"]
        url = article["url"]
        print(f"{i}: {title}, {url}")
