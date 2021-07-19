#!/usr/bin/env python3

import pyapikey
import requests

key = pyapikey.get_key("newsapi.org")

do_headlines = False
do_everything = True

if do_headlines:
    url = ('http://newsapi.org/v2/top-headlines?' 'country=us&' 'apiKey={}'.format(key))
    r = requests.get(url)
    r.raise_for_status()
    obj = r.json()

    articles = obj["articles"]
    for i, article in enumerate(articles):
        print("{}: {}".format(i, article["title"]))


import sys
if do_everything:
    param_q = 'qInTitle={}&'.format("corona")
    mydict = {
            'qInTitle': sys.argv[1],
            'pageSize': 20,
            'page': 1,
            'apiKey': key,
    }
    url = 'http://newsapi.org/v2/everything'
    r = requests.get(url, params=mydict)
    r.raise_for_status()
    obj = r.json()

    articles = obj["articles"]
    for i, article in enumerate(articles):
        print("{}: {}, {}".format(
            i,
            article["title"],
            article["url"],
        ))
