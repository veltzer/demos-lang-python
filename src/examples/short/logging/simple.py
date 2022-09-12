"""
Most basic logging example
"""

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.warning("this is a warning message %d", 1)
logger.debug("this is a debug message")
logger.info("this is an info message")
logger.error("this is an error message")
