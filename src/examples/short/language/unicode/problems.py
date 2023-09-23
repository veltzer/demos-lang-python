import sys
import codecs

ENCODING = "utf-8"
assert sys.stdout.encoding == ENCODING

# To make redirection work you need one of the following:
if sys.stdout.encoding is None:
    sys.stdout = codecs.getwriter(ENCODING)(sys.stdout)
# or this:
# $ export PYTHONIOENCODING=UTF-8
# in the environment

# lets show how to decode strings to bytes
data = "\xe9"
assert isinstance(data, str)
try:
    bytes(data, encoding=ENCODING)
except UnicodeEncodeError:
    pass

# this is the right way to decode data
t = data.encode(ENCODING)
assert isinstance(t, bytes)

# lets show how to print unicode data
print(f"this is data {data}")
