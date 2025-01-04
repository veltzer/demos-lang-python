#! /usr/bin/python

import re

def prep_row(row):
    row = re.sub(r"'", r"''", row)
    
    # Add quotes around each field using a Lambda function (alternative solution).
    # lrow = list((map(lambda f: "'" + f + "'", row.split(','))))
    
    lrow = []
    for field in row.split(","):
        lrow.append("'" + field + "'")
    
    return ",".join(lrow)
    
    
for row in open("country.txt", "r"):
    print(prep_row(row))

