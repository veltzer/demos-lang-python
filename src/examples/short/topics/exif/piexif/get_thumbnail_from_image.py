"""
This is an exmample of how to get the thumbnail EXIF data from an image that has a thumbnail
using the "piexif" python module.
"""

import os.path
import sys
import piexif

if len(sys.argv) != 3:
    print(f"{sys.argv[0]}: usage: {sys.argv[0]} [ORIGINAL_IMAGE] [TARGET_THUMBNAIL]")
    sys.exit(1)
original = sys.argv[1]
target = sys.argv[2]
assert not os.path.isfile(target), "target file should not exist"

exif_dict = piexif.load(original)
thumbnail = exif_dict.pop("thumbnail")
if thumbnail is not None:
    with open(target, "wb+") as f:
        f.write(thumbnail)
else:
    print("The image you gave me does not have a thumbnail!")
