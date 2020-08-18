"""
This is an example of how to read XML in python using the built in
xml.etree module

"""

import xml.etree.ElementTree

# both of these will work
mydoc = xml.etree.ElementTree.ElementTree(file='data_samples/data.xml')
# mydoc=xml.etree.ElementTree.parse('data_samples/data.xml')
for e in mydoc.findall('.//bar'):
    print(e.get('title'))
