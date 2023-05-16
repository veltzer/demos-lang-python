"""
This is a script that runs in a python specific version.
You can also see that via the output that it does.

In ubuntu you can install other versions of python this way:
sudo apt-get install python2.7
sudo apt-get install python3
/usr/bin/python in most distributions is just a symlink. It is
usually a bad idea to change that symlink since this is the
"default" python for the distribution. Remember that python is
used for a lot more in a modern distribution than just run your
code and so the default version should be determined by the
distribution vendor and not by you. If you want to use a different
version of python install it (either from the vendor if it"s available
or from binary or source code on your own) and use your own version
explicitly with the shbang line or environment variables,or maybe
absolute path on the command line.
"""

import sys

print("python version is", sys.version)
if sys.version_info[0:2] == (2, 7):
    print("version==2,7")
if sys.version_info[0:2] != (2, 7):
    print("version!=2,7")
else:
    print("version is not!=2,7")
if sys.version_info[0:2] > (2, 5):
    print("version>2,5")
if sys.version_info[0:2] < (3, 0):
    print("version<3,0")
if sys.version_info[0:2] > (2, 7):
    print("version>2,7")
else:
    print("version is not>2,7")
