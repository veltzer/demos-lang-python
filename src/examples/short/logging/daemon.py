"""
This is an example of how to configure the python logging system
to log to syslog

References:
- https://www.loggly.com/blog/new-style-daemons-python/
"""

import logging.handlers

name = "daemon"
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
handler = logging.handlers.SysLogHandler(address='/dev/log')
root_logger.addHandler(handler)
formatter = logging.Formatter(fmt=f"{name}[%(process)d]: %(levelname)s: %(message)s")
handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.debug("Debug")
logger.info("Info")
logger.warning("Warning")
