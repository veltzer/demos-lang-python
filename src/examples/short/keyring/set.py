"""
This is an example of setting a password.
"""

import keyring
keyring.set_password("dummyapp", "mark.veltzer@gmail.com", "thisisthepassword")
