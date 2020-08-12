import json
import urllib.request
import xml.etree.cElementTree as ElementTree

URL = 'http://ws.geonames.org/hierarchyJSON?geonameId=2657896'
places = json.loads(urllib.request.urlopen(URL).read())['geonames']

root = last = ElementTree.Element('place', name=places[0]['name'])
for place in places[1:]:
    last = ElementTree.SubElement(last, 'place', name=place['name'])

print(ElementTree.tostring(root))
