""" problems.py """

import codecs
import contextlib
import sys

ENCODING = "utf-8"
assert sys.stdout.encoding == ENCODING

# To make redirection work you need one of the following:
if sys.stdout.encoding is None:  # pyrefly: ignore[unnecessary-comparison]  teaching: the redirected-stdout case is the lesson
    sys.stdout = codecs.getwriter(ENCODING)(sys.stdout)
# or this:
# $ export PYTHONIOENCODING=UTF-8
# in the environment

# lets show how to decode strings to bytes
data = "\xe9"
assert isinstance(data, str)
with contextlib.suppress(UnicodeEncodeError):
    bytes(data, encoding=ENCODING)

# this is the right way to decode data
t = data.encode(ENCODING)
assert isinstance(t, bytes)

# lets show how to print unicode data
print(f"this is data {data}")
