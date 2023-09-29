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
    my_logger.setLevel(logging.WARNING)
    my_logger.warning("from the function: this is a warning message")
    my_logger.debug("from the function: this is a debug message")
    my_logger.info("from the function: this is an info message")
    my_logger.error("from the function: this is an error message")


logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)
logger.warning("this is a warning message")
logger.debug("this is a debug message")
logger.info("this is an info message")
logger.error("this is an error message")
my_function()
