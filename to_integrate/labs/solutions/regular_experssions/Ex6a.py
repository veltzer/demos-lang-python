#! /usr/bin/python
# Exercise 6, string formatting and regular expressions.
import re

infile = open('postcodes.txt', 'r')

# Variables for counting valid and invalid codes (part b)
valid = 0
invalid = 0

for postcode in infile:
    # The variable 'postcode' contain the line read from the file

    # Ignore empty lines.
    if postcode.isspace(): continue

    # (a): Remove newlines, tabs and spaces.
    postcode = re.sub('[ \t\n]', '', postcode)

    # (a): Convert to uppercase.
    postcode = postcode.upper()

    # (a): Insert a space before the final digit and 2 letters.
    postcode = re.sub('([0-9][A-Z]{2})$', r' \1', postcode)

    # Print the reformatted postcode.
    print(postcode)

    # TODO (b) Validate the postcode, returning a match object 'm'
    m = 0   # TODO (b) Replace this line with a call to re.match()
    
    if m:
        valid += 1
    else:
        invalid += 1
        

infile.close()

# TODO (b) Print the valid and invalid totals

