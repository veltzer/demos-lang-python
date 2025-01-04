#! /usr/bin/python
# Python 3 version

import struct
from myfile import MyFile
        
# Text file
class TextFile(MyFile):

    @property
    def contents(self):
        # Return the contents of the file
        return open(self.get_fname(), 'rt').read()
    
    @contents.setter
    def contents(self, value):
        # Append to the file
        if not value.endswith('\n'):
            value += '\n'
        open(self.get_fname(), 'at').write(value)
        return

# Binary file
class BinFile(MyFile):

    @property
    def contents(self):
        # Return the contents of the file
        value = open(self.get_fname(), 'rb').read()
        return value
    
    @contents.setter
    def contents(self, value):
        # Append to the file
        if isinstance(value, int):
            out = struct.pack('i', value)
            open(self.get_fname(), 'ab').write(out)
        else:
            open(self.get_fname(), 'ab').write(value.encode())
        return
        
if __name__ == '__main__':
    file1 = TextFile('file1.txt')
    print(file1, len(file1))

    file1.contents = 'hello'
    file1.contents = 'world'
    
    print(file1.contents)
    print("Size of file1:", len(file1))
 
    file2 = BinFile('file2.dat')
    print(file2, len(file2))

    file2.contents = 42
    file2.contents = 34
    file2.contents = 'EOD'

    print(file2.contents)
    print('Size of file2:', len(file2))
