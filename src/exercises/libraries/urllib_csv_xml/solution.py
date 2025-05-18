"""
Solution
"""

import csv
import urllib.request
# pylint: disable=deprecated-module
import xml.etree.cElementTree as ElementTree


def parse_feed(feed_string):
    rss = ElementTree.fromstring(feed_string)
    for item in rss.findall("channel/item"):
        date = item.findtext("pubDate")
        assert date is not None
        date = date.strip()
        title = item.findtext("title")
        assert title is not None
        package, version = title.split()
        description = item.findtext("description")
        yield date, package, version, description


def write_csv(filename, parsed_feed_string):
    with open(filename, "wb") as f:
        writer = csv.writer(f)
        writer.writerows(parsed_feed_string)


output = "/tmp/pypi.csv"
with urllib.request.urlopen("http://pypi.python.org/pypi?:action=rss") as stream:
    feed = stream.read()
parsed_feed = parse_feed(feed)
write_csv(output, parsed_feed)
print(f"wrote file [{output}]")
