"""
This example tries to show how to get rid of the scrapy logging.

Notes:
- in order to disable scrapy logging you need to pass "LOG_ENABLED":False
as a config option to the scrapy object. This will cause scrapy
to be totally silent.
- if you still want to see some logs you need to configure python logging
with the logger name "scrapy".
- you also need to configure the logging level of your own spider (in
this example "no_logging".
"""

import logging
from typing import Any, ClassVar

import scrapy.crawler

logger = logging.getLogger(__name__)


class SearchSpider(scrapy.Spider):
    name = __name__
    allowed_domains: ClassVar = [
        "jet.com"
    ]
    start_urls: ClassVar = [
        "https://jet.com/search/",
    ]

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """ constructor """
        super().__init__(*args, **kwargs)
        # important, call the parent
        self.logger.info("in __init__")

    def parse(self, _response, **_kwargs) -> None:
        """ This method is called whenever you get a response """
        self.logger.info("in parse")

    def closed(self, _reason) -> None:
        """
        This method is called automatically when the crawler finishes
        Note that because of python tricks this methods signature is different
        in the parent but this signature is the right one...
        """
        self.logger.info("in closed")


if __name__ == "__main__":
    logging.getLogger("scrapy").setLevel(logging.WARNING)
    logging.getLogger(__name__).setLevel(logging.WARNING)
    process = scrapy.crawler.CrawlerProcess({
        "LOG_ENABLED": False,
    })
    process.crawl(SearchSpider)
    process.start()
