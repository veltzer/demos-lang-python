#! /usr/bin/python

# Construct an index.
index = []
fh_in = open('messier.txt', 'r', encoding='latin_1')

while True:
    line = fh_in.readline()
    if not line: break
    if line.startswith('M'):
        num = line[1:6].rstrip()
        index.append(fh_in.tell() - len(line))

while True:
    num = input('Enter a Messier number to exit): ')
    if num.startswith('M'):
        num = int(num[1:])
    elif num:
        num = int(num)
    else:
        num = 0

    if num < 1: break
    num -= 1

    fh_in.seek(index[num])
    print(fh_in.readline())
