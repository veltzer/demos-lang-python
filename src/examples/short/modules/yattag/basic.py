"""
A basic example of how to use yattag.
"""

from yattag import Doc, indent

doc, tag, text = Doc().tagtext()

with tag("html"), tag("body"):
    with tag("p", id="main"):
        text("some text")
    with tag("a", href="/my-url"):
        text("some link")

result = doc.getvalue()
print(result)
pretty_html = indent(doc.getvalue())
print(pretty_html)
