"""
This is a simple example of how to use Scrapy

Note that this is an "in code" running of scrapy which *does not*
use the scrapy(1) command line tool. This is an integrated way
of running scrapy from within your code. There is another way
of running scrapy when all you are doing is scraping with a full
project structure and all. This is not that way.
"""

import scrapy.crawler


class SearchSpider(scrapy.Spider):
    name = __name__
    allowed_domains = [
        "google.com"
    ]
    start_urls = (
        "https://google.com",
    )

    def __init__(self, *args, **kwargs):
        """ constructor """
        # important, call the parent
        super().__init__(*args, **kwargs)
        self.logger.info("in __init__")

    def parse(self, _response, **_kwargs):
        """
        This method is called whenever you get a response
        """
        self.logger.info("in parse")
        # self.start_urls.append("https://safety.google/security-privacy/")
        yield scrapy.Request(url="https://google.com/maps", callback=self.parse)

    def closed(self, _reason):
        """
        This method is called automatically when the crawler finishes
        """
        self.logger.info("in closed")


if __name__ == "__main__":
    process = scrapy.crawler.CrawlerProcess()
    process.crawl(SearchSpider)
    process.start()
