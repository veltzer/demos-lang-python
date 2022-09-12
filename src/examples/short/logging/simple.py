"""
Most basic logging example

It seems that here I do not have to call:
        logging.basicConfig()
but in other examples I did need to call it....

Strange...
"""

import logging


def my_function():
    my_logger = logging.getLogger(__name__)
    my_logger.setLevel(logging.DEBUG)
    my_logger.warning("this is a warning message %d", 1)
    my_logger.debug("this is a debug message")
    my_logger.info("this is an info message")
    my_logger.error("this is an error message")


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.warning("this is a warning message %d", 1)
logger.debug("this is a debug message")
logger.info("this is an info message")
logger.error("this is an error message")
my_function()
