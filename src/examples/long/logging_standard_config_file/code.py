import logging.config

logging.config.fileConfig('logging.conf')
# logger = logging.getLogger(__name__)
logger = logging.getLogger('simple')

print(__name__)
logger.debug("this is a debug message")
logger.info("this is a info message")
