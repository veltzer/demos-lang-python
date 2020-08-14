import csv
import urllib.request
import xml.etree.cElementTree as ElementTree


def parse_feed(feed_string):
    rss = ElementTree.fromstring(feed_string)
    for item in rss.findall('channel/item'):
        date = item.findtext('pubDate').strip()
        package, version = item.findtext('title').split()
        description = item.findtext('description')
        yield date, package, version, description


def write_csv(filename, parsed_feed_string):
    with open(filename, 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(parsed_feed_string)


output = '/tmp/pypi.csv'
feed = urllib.request.urlopen('http://pypi.python.org/pypi?:action=rss').read()
parsed_feed = parse_feed(feed)
write_csv(output, parsed_feed)
print('wrote file [{0}]'.format(output))
