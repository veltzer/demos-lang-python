"""
This exmple explores how to undo what basicConfig does
"""

import logging
import logging_tree


logging_tree.printout()

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logging_tree.printout()

logger.warning("this is a warning message")
logger.debug("this is a debug message")

root_logger = logging.getLogger()
for x in root_logger.handlers:
    root_logger.removeHandler(x)

logging_tree.printout()

logger.warning("this is a warning message")
logger.debug("this is a debug message")
