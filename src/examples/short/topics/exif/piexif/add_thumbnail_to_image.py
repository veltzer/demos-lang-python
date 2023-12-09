"""
This is an example of how to read EXIF data using the "piexif" python module
"""

import os.path
import sys
from PIL import Image
import piexif

if len(sys.argv) != 4:
    print(f"{sys.argv[0]}: usage: {sys.argv[0]} [ORIGINAL_IMAGE] [THUMBNAIL] [TARGET_IMAGE]")
    sys.exit(1)
original = sys.argv[1]
thumbnail = sys.argv[2]
target = sys.argv[3]
with open(thumbnail, "rb") as thumbnail_stream:
    thumbnail_data = thumbnail_stream.read()
assert not os.path.isfile(target), "target file should not exist"
piexif_dict = piexif.load(original)
piexif_dict["thumbnail"] = thumbnail_data
piexif_dict["1st"][513] = 1  # JPEGInterchangeFormat
piexif_dict["1st"][514] = 1  # JPEGInterchangeFormatLength
piexif_bytes = piexif.dump(piexif_dict)
im = Image.open(original)
im.save(target, exif=piexif_bytes)
