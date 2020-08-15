"""
This is an example of how to configure the python logging system
to log to syslog

References:
- https://www.loggly.com/blog/new-style-daemons-python/
"""

import logging.handlers
from systemd.journal import JournalHandler

root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
handler = systemd.journal.JournalHanlder()
root_logger.addHandler(handler)

logger = logging.getLogger(__name__)
logger.debug("Debug")
logger.info("Info")
logger.warning("Warning")
