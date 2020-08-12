"""
Example of how to use the 'csv' module to write csv files
"""

import csv

data = [
    ['first, element', 5, ],
    ['second, element', 7, ],
]
with open('/tmp/output.csv', 'w') as csv_file_handle:
    w = csv.writer(csv_file_handle)
    for d in data:
        w.writerow(d)
