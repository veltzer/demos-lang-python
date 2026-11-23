"""
Usage: get_person.py "person_id"

Convert this script to imdbpy https://imdbpy.github.io/downloads/

NOTES:
- this script is python2 on purpose because the imdb module is currently only available for python2 in ubuntu.
"""

import sys

import imdb

if len(sys.argv) != 2:
    print(f"{sys.argv[0]}: usage: {sys.argv[0]} [person_id]", file=sys.stderr)
    print(f"{sys.argv[0]}: usage: {sys.argv[0]} 0124930", file=sys.stderr)
    print(f"{sys.argv[0]}: usage: {sys.argv[0]} 0000264 (for unicode)", file=sys.stderr)
    sys.exit(1)

person_id = sys.argv[1]
connection = imdb.IMDb()
out_encoding = sys.stdout.encoding or sys.getdefaultencoding()

person = connection.get_person(person_id)

i_canonical_name = person["canonical name"]
print(f"i_canonical_name is [{i_canonical_name.encode(out_encoding)}]")

for k, v in person.items():
    value = v.encode(out_encoding) if isinstance(v, str) else v
    print(f"[{k}],[{value}]")
