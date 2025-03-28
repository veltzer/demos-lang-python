""" search.py """

import sys
from azure.cognitiveservices.search.websearch import WebSearchClient
from msrest.authentication import CognitiveServicesCredentials

search = sys.argv[1]

subscription_key = "KEY_HERE"

client = WebSearchClient(
    endpoint="https://api.cognitive.microsoft.com",
    credentials=CognitiveServicesCredentials(subscription_key),
)

print(f"searching for [{search}]")
web_data = client.web.search(
    query=search,
    count=20,
)

if web_data.web_pages is None:
    print("have no web_pages results")
else:
    print(f"web search results will follow... (got [{len(web_data.web_pages.value)}] results)...")
    for i, val in enumerate(web_data.web_pages.value):
        print(f"{i} {val.name}")
        print(val.url)

if web_data.videos is None:
    print("have no video results")
else:
    print(f"video results will follow... (got [{len(web_data.videos.value)}] results)...")

if web_data.images is None:
    print("have no images results")
else:
    print(f"images results will follow... (got [{len(web_data.images.value)}] results)...")

if web_data.news is None:
    print("have no news results")
else:
    print(f"news results will follow... (got [{len(web_data.news.value)}] results)...")
    for i, val in enumerate(web_data.news.value):
        print(f"{i} {val.name}")
        print(val.url)
