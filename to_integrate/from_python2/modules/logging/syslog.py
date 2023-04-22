"""
This is an example of how to log to syslogd

- After running this look at /var/log/syslog to see
the output...
- the default formatter only logs the message without saying the level
and who the message came from
"""

import logging.handlers

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.handlers.SysLogHandler(address='/dev/log')
formatter = logging.Formatter('%(name)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.debug('this is debug')
logger.critical('this is critical')
