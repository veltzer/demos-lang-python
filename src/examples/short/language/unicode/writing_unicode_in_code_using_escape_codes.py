"""
This example shows how to use the "u" prefix to strings and the \\u escape in strings to create
multi lingual strings. All in all its better not to do all of this and keep multi lingual strings
out of the code and put it in some external source (database,config file,...).

In python2 you would have to put a "u" prefix but in python3 this is no longer needed since all
strings are unicode by default.
"""

print("\u05d4\u05d9")
# This is a snake (http://www.fileformat.info/info/unicode/char/1f40d/index.htm)
print("\U0001F40D")
# This is a cloud (http://www.fileformat.info/info/unicode/char/2601/index.htm)
print("\u2601")
