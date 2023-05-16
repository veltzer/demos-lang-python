"""
This is a basic logging example

NOTES:
- The idea of passing __name__ to the logger
is that you can turn logs on and off from certain modules.
- the first time you create a logger it doesnt have any handlers
and that"s why you don"t get any output despite the logging level
begin set correctly. if you turn off do_add_handler below you will
see no logging at debug level.
- to create another handler one must:
    create a handler
    set its level
    create a formatter
    set the formatting for the formatter
    attach the formatter to the handler
    add the handler to the logger
"""

import logging

import logging_tree

do_add_handler = True

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logging_tree.printout()
print(logger.handlers)

if do_add_handler:
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(name)s %(levelname)s %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

logger.warning("this is a warning message %d", 1)
logger.debug("this is a debug message")
