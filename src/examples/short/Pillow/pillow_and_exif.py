"""
This is an example of how to read EXIF data using the Pillow python module

References:
- https://stackoverflow.com/questions/4764932/in-python-how-do-i-read-the-exif-data-for-an-image
"""

import PIL.Image
import PIL.ExifTags

img = PIL.Image.open('data/jpg/image_with_exif.jpg')
exif_data = img.getexif()
for k, v in exif_data.items():
    string_tag = None
    if k in PIL.ExifTags.TAGS:
        string_tag = PIL.ExifTags.TAGS[k]
    print(f"{string_tag} {k} {v}")
# print(exif_data)
