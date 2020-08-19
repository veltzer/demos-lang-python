"""
This example shows how to read a csv file with python
"""

import csv

with open('data_samples/file.csv', 'r') as cvs_file:
    r = csv.reader(cvs_file)
    for row in r:
        print(row)
