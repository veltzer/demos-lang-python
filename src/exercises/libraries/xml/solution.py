import re
import xml.dom.minidom

dom = xml.dom.minidom.parse('data.xml')  # parse an XML file by name

for ticket in dom.getElementsByTagName('ImportTicket'):
    esr = ticket.getAttribute('external_system_reference')
    esr = re.sub('^0+', '', esr)
    ticket.setAttribute('external_system_reference', esr)

# print(dir(dom))
print(dom.toprettyxml())
# outfile=open('/tmp/result.xml','wb')
# dom.writexml(outfile)
