"""
This is an example of how to read XML in python using the built in
xml.etree module
"""

import xml.etree.ElementTree as ET

# both of these will work
doc_from_constructor = ET.ElementTree(file="data/xml/data.xml")
for e in doc_from_constructor.findall(".//bar"):
    print(e.get("title"))

# this will also work
doc_from_parse = ET.parse("data/xml/data.xml")
for e in doc_from_parse.findall(".//bar"):
    print(e.get("title"))
