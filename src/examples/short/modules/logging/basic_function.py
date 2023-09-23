"""
This example shows what happens when you log from a function

This shows that in the default configuration only the message
is shown without other info such as:
    - date
    - username
    - application name
    - function name
    - stack
"""

import logging


def my_func():
    logger = logging.getLogger()
    logger.error("hello")


my_func()
