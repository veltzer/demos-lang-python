"""
This example shows all possible EXIF fields

References:
- https://stackoverflow.com/questions/4764932/in-python-how-do-i-read-the-exif-data-for-an-image
"""

import PIL.ExifTags

for k, v in PIL.ExifTags.TAGS.items():
    print(k, v)
