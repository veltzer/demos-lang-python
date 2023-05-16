"""
This is an example that shows that configparser does NOT complain about
reading files which don"t exist.
Quite stupid.
"""

import configparser

c = configparser.ConfigParser()
c.read("non_exist.ini")
