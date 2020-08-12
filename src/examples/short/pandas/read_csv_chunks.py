"""
A demo of how to load a csv file
"""

import pandas

reader = pandas.read_csv("/etc/passwd", sep=":", chunksize=1)
line_count = 0
for chunk in reader:
    line_count += 1
    print(chunk.loc[0][0])
print("line_count is {}".format(line_count))
