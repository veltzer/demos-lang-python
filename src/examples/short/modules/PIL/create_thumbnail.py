"""
This is an example of who to create a thumbnail from an image using the "Pillow"
python library.

References:
- https://www.educative.io/answers/how-to-create-thumbnails-of-images-in-python
"""

import sys
from PIL import Image

SIZE_OF_THUMBNAIL = 75

if len(sys.argv) != 3:
    print(f"{sys.argv[0]}: usage: {sys.argv[0]} [LARGE_IMAGE] [THUMBNAIL]")
    sys.exit(1)

large_image = sys.argv[1]
thumbnail = sys.argv[2]
img = Image.open(large_image)
size = (SIZE_OF_THUMBNAIL, SIZE_OF_THUMBNAIL)
img.thumbnail(size)
img.save(thumbnail)
