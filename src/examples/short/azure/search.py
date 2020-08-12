import sys
from azure.cognitiveservices.search.websearch import WebSearchClient
from azure.cognitiveservices.search.websearch.models import SafeSearch
from msrest.authentication import CognitiveServicesCredentials

search=sys.argv[1]

subscription_key = "KEY_HERE"

client = WebSearchClient(
        endpoint="https://api.cognitive.microsoft.com",
        credentials=CognitiveServicesCredentials(subscription_key),
) 

print("searching for [{}]".format(search))
web_data = client.web.search(
        query=search,
        count=20,
)

if web_data.web_pages is None:
    print("have no web_pages results")
else:
    print("web search results will follow... (got [{}] results)...".format(len(web_data.web_pages.value)))
    for i, val in enumerate(web_data.web_pages.value):
        print("{} {}".format(i, val.name))
        print(val.url)

if web_data.videos is None:
    print("have no video results")
else:
    print("video results will follow... (got [{}] results)...".format(len(web_data.videos.value)))

if web_data.images is None:
    print("have no images results")
else:
    print("images results will follow... (got [{}] results)...".format(len(web_data.images.value)))

if web_data.news is None:
    print("have no news results")
else:
    print("news results will follow... (got [{}] results)...".format(len(web_data.news.value)))
    for i, val in enumerate(web_data.news.value):
        print("{} {}".format(i, val.name))
        print(val.url)
