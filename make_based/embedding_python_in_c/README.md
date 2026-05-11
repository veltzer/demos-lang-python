# Embedding Python in C

This is an example showing how to run python *within* your C program via the `libpython`
library supplied by the python developers.

Notes:
* if you do not want to hardcode paths in your build system to where the python include files and libraries are then you can use the python2.X-config utility supplied with python to give you the information that you need. You should really use it if you want your build system to work across different types of the Linux which have different versions of python and store its files in different folders.
* the example goes to sleep for 60 seconds to give you a chance to example the operating system information and see that indeed there is only one thread for your application. This proves that python runs IN YOUR OWN THREAD.

TODO:
* examples of opening threads in python AND in C and these threads co-existing in one C application.
