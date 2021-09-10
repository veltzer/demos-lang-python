"""
This is a demo of how to use the lzma module to open compressed files.

This demos shows that the lzma builtin python library only supports
the "xz" format.
"""

import lzma

try:
    with lzma.open("data/xz/file.xz", "rt") as file_handle:
        for line in file_handle:
            print(line, end="")
except lzma.LZMAError as e:
    print("yes, xz is not supported by the lzma")

try:
    with lzma.open("data/gz/file.gz", "rt") as file_handle:
        for line in file_handle:
            print(line, end="")
except lzma.LZMAError as e:
    print("yes, gz is not supported by the lzma")

try:
    with lzma.open("data/bz2/file.bz2", "rt") as file_handle:
        for line in file_handle:
            print(line, end="")
except lzma.LZMAError as e:
    print("yes, bz2 is not supported by the lzma")

try:
    with lzma.open("data/txt/file.txt", "rt") as file_handle:
        for line in file_handle:
            print(line, end="")
except lzma.LZMAError as e:
    print("yes, plain text is not supported by the lzma")
