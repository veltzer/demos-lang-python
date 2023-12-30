"""
This script shows statistic are number of tags that exiftools finds per folder.
It only scans ".mkv" files in that folder.
"""

import os
import os.path
import sys
import subprocess

import statistics


def get_suffix(filename:str) -> str:
    return os.path.splitext(filename)[1]


def get_number_of_exiftool_tags(filename: str) -> int:
    output = subprocess.check_output(["exiftool", filename], shell=False)
    lines = output.decode("ascii").splitlines()
    return len(lines)


if len(sys.argv) != 2:
    print(f"{sys.argv[0]}: usage: {sys.argv[0]} [FOLDER_NAME]")
    sys.exit(1)

folder_name = sys.argv[1]

# recursively traverse all files in the folder
for root, directories, files in os.walk(folder_name):
    tag_numbers = []
    for file in files:
        full = os.path.join(root, file)
        # if the file ends with ".mkv" add scan it with exiftool and add the number of tags
        # seen to the statistics
        suffix = get_suffix(full)
        if suffix != ".mkv":
            continue
        print(f"scanning [{full}]")
        tag_number = get_number_of_exiftool_tags(full)
        tag_numbers.append(tag_number)
print(f"min: {min(tag_numbers)}")
print(f"max: {max(tag_numbers)}")
print(f"mean: {statistics.mean(tag_numbers)}")
print(f"stdev: {statistics.stdev(tag_numbers)}")
print(f"median: {statistics.median(tag_numbers)}")
