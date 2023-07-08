"""
This example run the exiftool(1) tool with the -list flag and creates a file with all exif tag
names from it.

Why do we need it?
Because it turns out THERE IS NO LIST OF ALL POSSIBLE EXIF TAGS!!!
I know! This is absurd!
I couldn't find such a list on the web.

The problem is that the output of exiftool(1) is for human consumption and not for computer
use so we need to run "exiftool -list" and masssage the output a little bit.
"""

import subprocess

output = subprocess.check_output(["exiftool", "-list"], shell=False)
lines = output.decode("ascii").splitlines()
tags_all = set()
for line in lines:
    line = line.rstrip()
    if line == "Available tags:":
        continue
    if line == "Command-line shortcuts:":
        break
    current_line_tags = line.split()
    for current_line_tag in current_line_tags:
        tags_all.add(current_line_tag)
print(f"I got [{len(tags_all)}] tags_all")
with open("data/exif/tags_all.txt", "wt") as stream:
    for tag in sorted(tags_all):
        stream.write(f"{tag}\n")

# run exiftool on an image without exif tags and record all non exif tags
output = subprocess.check_output(["exiftool", "data/exif/image_stripped_by_exiftool.jpg"], shell=False)
lines = output.decode("ascii").splitlines()
tags_non_exif = set()
for line in lines:
    line = line.rstrip()
    current_tag = line.split(":")[0].rstrip()
    tags_non_exif.add(current_tag)
print(f"I got [{len(tags_non_exif)}] tags_non_exif")
with open("data/exif/tags_non_exif.txt", "wt") as stream:
    for tag in sorted(tags_non_exif):
        stream.write(f"{tag}\n")

tags_both = tags_all.intersection(tags_non_exif)
print(f"I got [{len(tags_both)}] tags_both")
with open("data/exif/tags_both.txt", "wt") as stream:
    for tag in sorted(tags_both):
        stream.write(f"{tag}\n")

tags_exif = tags_all - tags_non_exif
print(f"I got [{len(tags_exif)}] tags_exif")
with open("data/exif/tags_exif.txt", "wt") as stream:
    for tag in sorted(tags_exif):
        stream.write(f"{tag}\n")
