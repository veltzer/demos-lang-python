"""
This is an example that shows all EXIF fields that the ExifRead python module knows.
"""

import exifread

print(dir(exifread))
print(dir(exifread.tags))
print(exifread.tags.EXIF_TAGS)
