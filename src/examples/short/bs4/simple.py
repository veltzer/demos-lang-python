"""
A simple demos for BeautifulSoup

References:
- https://www.topcoder.com/thrive/articles/web-scraping-with-beautiful-soup
"""

from bs4 import BeautifulSoup
import requests

url_link = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"
r = requests.get(url_link, timeout=5)
r.raise_for_status()
doc = BeautifulSoup(r.text, "html.parser")
print(doc.prettify())
