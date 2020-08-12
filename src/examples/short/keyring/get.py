"""
A basic example of how to get a password from the default
keyring of you environment.
"""

import keyring
password = keyring.get_password(u"dummyapp", u"mark.veltzer@gmail.com")
print("your password is [{}]".format(password))
