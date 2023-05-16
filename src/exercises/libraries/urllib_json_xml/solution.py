import json
import urllib.request
# pylint: disable=deprecated-module
import xml.etree.cElementTree as ElementTree

URL = "http://ws.geonames.org/hierarchyJSON?geonameId=2657896"
with urllib.request.urlopen(URL) as stream:
    places = json.loads(stream.read())["geonames"]

root = last = ElementTree.Element("place", name=places[0]["name"])
for place in places[1:]:
    last = ElementTree.SubElement(last, "place", name=place["name"])

print(ElementTree.tostring(root))
