"""
This is how you want to use the logging module in a small script.

The key is the logging.basicConfig method to setup the config
for basic usage.

The problem with this example is that you set your own logging
level which is contrary to logging philosophy. You should not
set your own logging level.

Another issue is that if you throw an exception it DOES NOT
get logged with a logger but rather through prints.
"""

import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.warning("this is a warning message %d", 1)
logger.debug("this is a debug message")

raise ValueError("this is an error")
