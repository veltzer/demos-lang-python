"""
This is an example of how to read EXIF data using the ExifRead python module
"""

import sys
import exifread

if len(sys.argv) != 2:
    print(f"{sys.argv[0]}: usage: {sys.argv[0]} [IMAGE_FILENAME]")
    sys.exit(1)
image_name = sys.argv[1]
with open(image_name, "rb") as stream:
    tags = exifread.process_file(stream)
    for k, v in tags.items():
        v_str = str(v)
        v_str = v_str[:10]
        k_str = str(k)
        print(f"{k_str}: {v_str}")
