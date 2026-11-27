""" code.py """

import logging.config

logging.config.fileConfig("logging.conf")
# logger = logging.getLogger(__name__)  # noqa: ERA001  teaching: kept in the comment for the reader
logger = logging.getLogger("simple")

print(__name__)
logger.debug("this is a debug message")
logger.info("this is a info message")
