# Reading a static file from inside a package

There are three ways shown here:
* python module `importlib.resources` which *is* in the python standard library.
* own hand crafted code.
* `pkgutil` which is in the standard library.

Note: older versions of this example used `pkg_resources` (from `setuptools`).
That module was removed in `setuptools` 82, and `importlib.resources` is the
modern replacement for it.

References:
* [Stack Overflow: Python — how to read a static file from inside a package](http://stackoverflow.com/questions/6028000/python-how-to-read-a-static-file-from-inside-a-package)
