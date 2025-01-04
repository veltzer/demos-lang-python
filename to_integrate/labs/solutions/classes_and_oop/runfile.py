#!/usr/local/bin/python

from myfile import MyFile

filea = MyFile("country.txt")
print(filea)

print(filea.get_fname(), "is", len(filea), "bytes")
