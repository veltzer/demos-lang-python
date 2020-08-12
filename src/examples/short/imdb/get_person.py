"""
Usage: get_person.py 'personID'

NOTES:
- this script is python2 on purpose because the imdb module is currently only available for python2 in ubuntu.
"""

import sys

import imdb

if len(sys.argv) != 2:
    print('{0}: usage: {0} [personID]'.format(sys.argv[0]))
    print('{0}: usage: {0} 0124930'.format(sys.argv[0]))
    print('{0}: usage: {0} 0000264 (for unicode)'.format(sys.argv[0]))
    sys.exit(1)

personID = sys.argv[1]
connection = imdb.IMDb()
out_encoding = sys.stdout.encoding or sys.getdefaultencoding()

person = connection.get_person(personID)

i_canonical_name = person['canonical name']
print('i_canonical_name is [{0}]'.format(
    i_canonical_name.encode(out_encoding)))

for k, v in person.items():
    if isinstance(v, unicode):
        v = v.encode(out_encoding)
    print('[{0}],[{1}]'.format(k, v))
