"""
Solutiion
"""

import json
import urllib.request
from xml.etree import ElementTree as ET

URL = "http://ws.geonames.org/hierarchyJSON?geonameId=2657896"
with urllib.request.urlopen(URL) as stream:
    places = json.loads(stream.read())["geonames"]

root = last = ET.Element("place", name=places[0]["name"])
for place in places[1:]:
    last = ET.SubElement(last, "place", name=place["name"])

print(ET.tostring(root))
