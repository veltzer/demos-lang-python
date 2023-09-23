"""
This example shows how to correctly write a newline charcter
in python in a way which is operating system portable.

References:
- http://stackoverflow.com/questions/1223289/how-to-write-native-newline-character-to-a-file-descriptor-in-python
"""

import os

print("Hello World", end="")
print(os.linesep, end="")
