import logging
import logging.config

import correct
import incorrect
import yaml


def main():
    with open("config.yaml", "rt") as input_handle:
        config = yaml.safe_load(input_handle.read())
    logging.config.dictConfig(config)
    logger = logging.getLogger(__name__)
    logger.info("before")
    correct.demo()
    incorrect.demo()
    logger.info("after")


if __name__ == "__main__":
    main()
