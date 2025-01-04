#! /usr/bin/python

import os.path

class MyFile:
   def __init__(self, filename):
       self._fname = filename

   def __str__(self):
       s = open(self._fname, 'r').read()
       return s

   def __len__(self):
       return os.path.getsize(self._fname)

   def get_fname(self):
       return self._fname
  
