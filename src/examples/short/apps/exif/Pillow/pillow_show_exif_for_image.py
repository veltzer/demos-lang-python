"""
This is an example of how to read EXIF data using the Pillow python module

References:
- https://stackoverflow.com/questions/4764932/in-python-how-do-i-read-the-exif-data-for-an-image
"""

import sys
import PIL.Image
import PIL.ExifTags

if len(sys.argv) != 2:
    print(f"{sys.argv[0]}: usage: {sys.argv[0]} [IMAGE_FILENAME]")
    sys.exit(1)
image_name = sys.argv[1]
image = PIL.Image.open(image_name)
exif_data = image.getexif()
# print(exif_data)
for k, v in exif_data.items():
    string_tag = None
    if k in PIL.ExifTags.TAGS:
        string_tag = PIL.ExifTags.TAGS[k]
    print(f"{string_tag} {k} {v}")
exif_data = image.info["exif"]
print(type(exif_data))
# print(exif_data)
