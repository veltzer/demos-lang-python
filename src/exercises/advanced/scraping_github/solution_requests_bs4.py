import requests
from bs4 import BeautifulSoup


"""
We are looking for the following html fragment:
     <h1 class="h0-mktg mt-sm-6 mt-md-11 mt-lg-9 mb-2 mb-sm-4 position-relative z-2">                                                Let’s build from here                                                                                                         </h1>
"""

url = "http://github.com"
r = requests.get(url, timeout=5)
r.raise_for_status()
doc = BeautifulSoup(r.text, "html.parser")
# print(doc.prettify())
my_list = doc.find_all(name="h1", attrs={"class": "h0-mktg"})
assert len(my_list) == 1, "found more than 1 element, please narrow your search"
my_element = my_list[0]
# print(dir(my_element))
print(my_element.contents[0].strip())
