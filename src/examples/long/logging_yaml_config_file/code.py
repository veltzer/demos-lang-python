import logging.config

import yaml

"""
This is how to load a yaml file as configuration for python logging
"""
with open('logging.yaml') as f:
    config = yaml.load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger('simple')

print(__name__)
logger.debug("this is a debug message")
logger.info("this is a info message")
