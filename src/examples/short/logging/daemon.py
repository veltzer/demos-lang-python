"""
This is an example of how to configure the python logging system
to log to syslog

References:
- https://www.loggly.com/blog/new-style-daemons-python/
"""

import logging
import logging.handlers

name = "foobar"
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
handler = logging.handlers.SysLogHandler(address='/dev/log')
root_logger.addHandler(handler)
formatter = logging.Formatter(fmt='{}[%(process)d]: %(levelname)s: %(message)s'.format(name))
handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.debug("Debug")
logger.info("Info")
logger.warning("Warning")
