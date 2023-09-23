"""
This is an example of a simple stream in Python
"""

FILENAME = "/etc/passwd"

with open(FILENAME) as stream:
    count = 0
    for line in stream:
        count += 1
    print(f"number of lines in file is {count}")
