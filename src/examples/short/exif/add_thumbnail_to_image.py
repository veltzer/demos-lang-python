"""
This is an example of how to read EXIF data using the 'exif' python module
"""

import os.path
import sys
from exif import Image

if len(sys.argv) != 3:
    print(f"{sys.argv[0]}: usage: {sys.argv[0]} [ORIGINAL_IMAGE] [TARGET_IMAGE]")
    sys.exit(1)
original = sys.argv[1]
target = sys.argv[2]
assert not os.path.isfile(target), "target file should not exist"
with open(original, 'rb') as image_file:
    image = Image(image_file)
    image["Thumbnail"] = "thumbnail data"
    with open(target, 'wb') as target_stream:
        target_stream.write(image.get_file())
