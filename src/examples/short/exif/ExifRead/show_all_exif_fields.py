"""
This is an example that shows all EXIF fields that the ExifRead python module knows.
"""

import exifread

# print(dir(exifread))
# print(dir(exifread.tags))
# print(type(exifread.tags.EXIF_TAGS))
# print(exifread.tags.EXIF_TAGS)
for k,v in exifread.tags.EXIF_TAGS.items():
    print(v[0])
    # print(k, v)
