import sys
import codecs

assert sys.stdout.encoding=="UTF-8"

# To make redirection work you need one of the following:
if sys.stdout.encoding is None:
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout)
# or this:
# $ export PYTHONIOENCODING=UTF-8
# in the environment

# lets show how to decode unicode data
data = u"\xe9"
assert type(data) == unicode
try:
    bytes(data)
except UnicodeEncodeError:
    pass

# this is the right way to decode data (the type of the output is "str"
# which is python 2 version of "bytes")
t = data.encode("utf-8")
assert type(t) == str

# lets show how to print unicode data
print(data)
# this will not work because the encoder will be ascii
try:
    print("this is data {}".format(data))
except UnicodeEncodeError:
    pass
print(u"this works ok {}".format(data))
