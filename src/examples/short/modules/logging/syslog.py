"""
This is an example of how to use the python `logging` module to log to syslogd

- After running this look at /var/log/syslog to see
the output...
- the default formatter only logs the message without saying the level
and who the message came from
"""

import time
import logging.handlers

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.handlers.SysLogHandler(address="/dev/log")
formatter = logging.Formatter("%(name)s %(levelname)s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

print("please run 'tail -f /var/log/syslog' to see the logs...")
counter = 0
while True:
    logger.debug(f"this is debug {counter}")
    logger.critical(f"this is critical {counter}")
    counter += 1
    time.sleep(1)

# os.system("tail /var/log/syslog")
