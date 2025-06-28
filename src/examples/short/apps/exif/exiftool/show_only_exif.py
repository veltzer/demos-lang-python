"""
This script shows ONLY exif data from a file.
If it shows nothing then this file does not have any EXIF data.

References:
- https://stackoverflow.com/questions/60576891/how-to-read-exif-data-of-movies-in-python
"""

import sys
import subprocess

if len(sys.argv) != 2:
    print(f"{sys.argv[0]}: usage: {sys.argv[0]} [FILENAME]")
    sys.exit(1)

filename = sys.argv[1]

with open("data/exif/tags_non_exif.txt") as stream:
    tags_non_exif = {line.strip() for line in stream}

output = subprocess.check_output(["exiftool", filename], shell=False)
lines = output.decode("ascii").splitlines()
for line in lines:
    line = line.rstrip()
    current_tag = line.split(":")[0].rstrip()
    if current_tag in tags_non_exif:
        continue
    print(line)
