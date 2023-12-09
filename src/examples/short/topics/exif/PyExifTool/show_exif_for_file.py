"""
This example shows all possible EXIF fields using the "PyExifTool" python module.
"""

import sys

import exiftool


if len(sys.argv) != 2:
    print(f"{sys.argv[0]}: usage: {sys.argv[0]} [FILENAME]")
    sys.exit(1)

filename = sys.argv[1]

with exiftool.ExifToolHelper() as et:
    metadata = et.get_metadata(filename)
    for d in metadata:
        for k, v in d.items():
            print(k, v)
    # print(help(et.get_tags))
    # tags = et.get_tags(filename)
    # print(tags)
