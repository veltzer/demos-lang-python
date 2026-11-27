"""
Solution
"""

import logging
import logging.handlers
import os

import logging_tree

logging.basicConfig()

# get the root logger, and remove its handler
logging.root.handlers.clear()

# logger1 configuration
logger1 = logging.getLogger("name1")
# logger1.propagate = False  # noqa: ERA001  teaching: kept in the comment for the reader
file_handler = logging.FileHandler("/tmp/log.txt")
logger1.addHandler(file_handler)
logger1.setLevel(logging.WARNING)

# logger2 configuration
logger2 = logging.getLogger("name2")
# logger2.propagate = False  # noqa: ERA001  teaching: kept in the comment for the reader
# while logger2.hasHandlers():
#     logger2.removeHandler(logger2.handlers[0])  # noqa: ERA001  teaching: kept in the comment for the reader
handler = logging.handlers.SysLogHandler(address="/dev/log")
logger2.addHandler(handler)
logger2.setLevel(logging.DEBUG)

# logger3 -> it will be a child logger of logger2
logger3 = logger2.getChild("name3")

# lets print the logging tree
logging_tree.printout()

# now lets see how our loggers work
logger1.error("this is an error message %s", os.getpid())
logger1.debug("this is a debug message %s", os.getpid())
logger2.error("this is an error message %s", os.getpid())
logger2.debug("this is a debug message %s", os.getpid())
logger3.error("this is an error message %s", os.getpid())
logger3.debug("this is a debug message %s", os.getpid())
