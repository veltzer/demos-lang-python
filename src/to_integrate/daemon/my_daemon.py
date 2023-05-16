import logging.handlers
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.handlers.SysLogHandler(address="/dev/log")
formatter = logging.Formatter("%(name)s %(levelname)s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


i = 0
while True:
    logger.debug(f"this is debug mesage {i}")
    i += 1
    time.sleep(5)
