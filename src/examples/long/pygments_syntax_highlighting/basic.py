"""
Basic coloring with pygments
"""

import sys

from pygments import highlight
# pylint: disable=no-name-in-module
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer

css_filename = "out.css"
html_filename = "out.html"
html_header = f"""<html>
<head>
<link rel="stylesheet" href="{css_filename}"/>
</head>
<body>
"""
html_footer = """
</body>
"""
my_class = "highlighter"

#
# code #
#
formatter = HtmlFormatter(linenos=True, cssclass=my_class)
with open(css_filename, "w") as f_css:
    f_css.write(formatter.get_style_defs("." + my_class))
with open(sys.argv[0]) as stream:
    code = stream.read()
with open(html_filename, "w") as f_html:
    f_html.write(html_header)
    highlight(code, PythonLexer(), formatter, f_html)
    f_html.write(html_footer)
