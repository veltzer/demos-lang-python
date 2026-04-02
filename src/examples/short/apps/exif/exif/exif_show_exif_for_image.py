"""
This is an example of how to read EXIF data using the "exif" python module
"""

import sys
from exif import Image

if len(sys.argv) != 2:
    print(f"{sys.argv[0]}: usage: {sys.argv[0]} [IMAGE_FILENAME]")
    sys.exit(1)
image_name = sys.argv[1]
with open(image_name, "rb") as image_file:
    image = Image(image_file)
    # print(image.has_exif)
    for field in image.list_all():
        print(field)
