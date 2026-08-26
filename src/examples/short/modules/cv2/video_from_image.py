"""
This script converts a single image to a video.
Try it with an .jpg input and a .avi output

References:
- https://stackoverflow.com/questions/44947505/how-to-make-a-movie-out-of-images-in-python
"""


import sys

import cv2

if len(sys.argv) != 3:
    print(f"{sys.argv[0]}: usage: {sys.argv[0]} [IMAGE] [VIDEO]")
    sys.exit(1)

image = sys.argv[1]
video = sys.argv[2]

images = [image]
frame = cv2.imread(image)
# imread returns None when the file is missing or is not a decodable image,
# so check before using it - otherwise this fails with a confusing
# AttributeError on None.
if frame is None:
    print(f"{sys.argv[0]}: could not read image [{image}]")
    sys.exit(1)
height, width, layers = frame.shape

video_writer = cv2.VideoWriter(video, 0, 1, (width,height))

for image in images:
    image_frame = cv2.imread(image)
    if image_frame is None:
        print(f"{sys.argv[0]}: could not read image [{image}]")
        sys.exit(1)
    video_writer.write(image_frame)

cv2.destroyAllWindows()
video_writer.release()
