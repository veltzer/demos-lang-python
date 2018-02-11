#!/usr/bin/env python

"""
This example shows how to read a csv utf file in python3 using the
built in 'csv' module.

NOTES:
- it turns out that in python3 it is not imperative to pass the
'encoding' flag to 'open' in order to have the file open in utf-8.
- the 'open' function opens with encding 'locale.getpreferredendoing()'
which is UTF-8 as far as I can tell.
- this looks independent of the PYTHONIOENCODING environment variable.

References:
- https://docs.python.org/3/library/locale.html#locale.getpreferredencoding
- https://docs.python.org/3/library/functions.html#open
"""

import csv
import locale


print(locale.getpreferredencoding())

# open a regular file with the utf-8 encoing works
with open('data_samples/file.csv', 'r', encoding='utf-8') as csvfile:
    r = csv.reader(csvfile)
    for row in r:
        pass

# now lets try reading a real utf file
with open('data_samples/file_utf.csv', 'r', encoding='utf-8') as csvfile:
    r = csv.reader(csvfile)
    for row in r:
        pass

# now lets try reading a real utf file without the encoding
with open('data_samples/file_utf.csv', 'r') as csvfile:
    r = csv.reader(csvfile)
    for row in r:
        print(row)
