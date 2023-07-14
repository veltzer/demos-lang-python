"""
This example shows how to silence logger for a piece of code.
"""

import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.error("This you should see")

logging.disable(logging.CRITICAL)
logger.error("This you should not see")
logging.disable(logging.NOTSET)

logger.error("This you should see")
