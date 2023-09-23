"""
This is an example of how to read XML in python using the built in
xml.etree module
"""

import xml.etree.ElementTree


# both of these will work
doc = xml.etree.ElementTree.ElementTree(file="data/xml/data.xml")
for e in doc.findall(".//bar"):
    print(e.get("title"))

# this will also work
doc = xml.etree.ElementTree.parse("data/xml/data.xml")
for e in doc.findall(".//bar"):
    print(e.get("title"))
