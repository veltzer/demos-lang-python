"""
This is an example of how to read a csv file with header.

References:
- https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/
"""

import pandas

filename = "data_samples/file.csv"
df = pandas.read_csv(filename)
print df.head()
