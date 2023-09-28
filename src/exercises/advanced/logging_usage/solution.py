import logging
import os
import logging.handlers

logging.basicConfig()

# logger1 configuration
logger1 = logging.getLogger("name1")
logger1.propagate = False
file_handler = logging.FileHandler('/tmp/log.txt')
logger1.addHandler(file_handler)
logger1.setLevel(logging.WARNING)

# logger2 configuration
logger2 = logging.getLogger("name2")
logger2.propagate = False
# while logger2.hasHandlers():
#     logger2.removeHandler(logger2.handlers[0])
handler = logging.handlers.SysLogHandler(address="/dev/log")
logger2.addHandler(handler)
logger2.setLevel(logging.DEBUG)

# now lets see how our loggers work
logger1.error(f"this is an error message {os.getpid()}")
logger1.debug(f"this is a debug message {os.getpid()}")
logger2.error(f"this is an error message {os.getpid()}")
logger2.debug(f"this is a debug message {os.getpid()}")
