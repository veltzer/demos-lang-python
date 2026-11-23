"""
This example shows how to remove whitespace elements from an ElementTree based dom.

References:
http://stackoverflow.com/questions/1098118/stripping-spaces-between-xml-nodes-with-python
"""

import re
import xml.etree.ElementTree as ET

whitespaces = re.compile(r"\s+")

"""
def omit_whitespaces(iter):
    for event, elem in iter:
        if whitespaces.match(elem.text):
            elem.text=""
        if elem.tail is not None and whitespaces.match(elem.tail):
            elem.tail=""
        yield event,elem

for event, elem in omit_whitespaces(ET.iterparse("data/xml/data.xml")):
    if elem.tag=="root":
        print(ET.tostring(elem))
"""

dom = ET.parse("data/xml/data.xml")
for elem in dom.getroot().iter():
    assert elem.text is not None
    if whitespaces.match(elem.text):
        elem.text = ""
    if elem.tail is not None and whitespaces.match(elem.tail):
        elem.tail = ""
print(ET.tostring(dom.getroot()))
