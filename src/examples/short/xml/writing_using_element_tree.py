"""
This is an example of how to writing XML in python using the built in
xml.etree module

The only problem with this is that xml.etree.ElementTree does not know how
to pretty output xml and so I do the corretion using xml.dom.minidom at
the bottom.
"""

import io
import xml
from xml.etree import ElementTree

root = ElementTree.Element("root")
doc = ElementTree.SubElement(root, "doc")

field1 = ElementTree.SubElement(doc, "field1")
field1.set("name", "name of field1")
field1.text = "field 1 free text"

field1 = ElementTree.SubElement(doc, "field2")
field1.set("name", "name of field2")
field1.text = "field 2 free text"

tree = ElementTree.ElementTree(root)
f = io.BytesIO()
tree.write(f)
f.seek(0)

# lets fixup the xml by overwriting the file with the pretty version
xml = xml.dom.minidom.parse(f)  # type: ignore
pretty_xml = xml.toprettyxml()  # type: ignore
print(pretty_xml)
