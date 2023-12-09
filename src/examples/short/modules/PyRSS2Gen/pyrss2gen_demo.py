"""
TBD: demo of how to use the PyRSS2Gen module.

References:
- http://www.dalkescientific.com/Python/PyRSS2Gen.html
"""

import datetime
import PyRSS2Gen


rss = PyRSS2Gen.RSS2(
    title="Andrews PyRSS2Gen feed",
    link="http://www.dalkescientific.com/Python/PyRSS2Gen.html",
    description="The latest news about PyRSS2Gen, a Python library for generating RSS2 feeds",
    lastBuildDate=datetime.datetime.now(),
    items=[
        PyRSS2Gen.RSSItem(
            title="PyRSS2Gen-0.0 released",
            link="http://www.dalkescientific.com/news/030906-PyRSS2Gen.html",
            description="Dalke Scientific today announced PyRSS2Gen-0.0",
            guid=PyRSS2Gen.Guid("http://www.dalkescientific.com/news/"),
            pubDate=datetime.datetime(2003, 9, 6, 21, 31)
        ),
        PyRSS2Gen.RSSItem(
            title="Thoughts on RSS feeds for bioinformatics",
            link="http://www.dalkescientific.com/writings/diary/",
            description="One of the reasons I wrote PyRSS2Gen was to ",
            guid=PyRSS2Gen.Guid("http://www.dalkescientific.com/writings/"),
            pubDate=datetime.datetime(2003, 9, 6, 21, 49)
        )
    ])

with open("/tmp/pyrss2gen.xml", "w") as stream:
    rss.write_xml(stream)
