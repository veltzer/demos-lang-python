"""
This example explores how logging behaves if no special
configuration is performed.

conclusions:
- we get an error printout which DOES NOT stop the program
    that we do not have handlers.
    "No handlers could be found for logger "root""
    This is printed once and then no more.
    this is true for both "__main__" and "root" which is
    the logger you get when you do 'logging.getLogger()'
"""

import logging

# logger = logging.getLogger(__name__)
logger = logging.getLogger()
print("warning")
logger.warning("this is a warning message")
print("debug")
logger.debug("this is a debug message")
print("error")
logger.error("this is an error message")
