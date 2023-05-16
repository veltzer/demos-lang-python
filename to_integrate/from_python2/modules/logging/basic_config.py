"""
This is how you want to use the logging module in a small script.

NOTES:
- if you don"t configure logging through other means, or call
"basicConfig" you will get warnings when you try to log (no handlers).
- if you dont pass the "level" parameter to "basicConfig" you
will get the default level which is WARNING (pretty good).
- don"t do "logger.setLevel". This is contrary to logging philosophy.
"""

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.debug("before")
logger.info("before")
logger.warning("before")
logger.error("before")

# logging.basicConfig(level=logging.WARNING)
logging.basicConfig()

logger.debug("after")
logger.info("after")
logger.warning("after")
logger.error("after")
