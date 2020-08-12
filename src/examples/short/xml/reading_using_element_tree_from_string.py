"""
This is an example of how to read XML in python using the built in
xml.etree module

The reason this example uses the 'io.StringIO' stuff is so that we
could embed the xml in the example and not put it in a file.
"""

import io
import xml.etree.ElementTree

data = '''
<root>
    <foo>
        <bar title='this is the text you are looking for'>
            bar content
        </bar>
    </foo>
</root>
'''

file = io.StringIO(data)

# both of these will work
# mydoc=xml.etree.ElementTree.ElementTree(file=file)
mydoc = xml.etree.ElementTree.parse(file)
for e in mydoc.findall('.//bar'):
    print(e.get('title'))
