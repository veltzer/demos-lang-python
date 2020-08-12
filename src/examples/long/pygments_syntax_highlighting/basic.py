"""
Basic coloring with pygments
"""

import sys

from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer

#
# paramters #
#
css_filename = 'out.css'
html_filename = 'out.html'
html_header = '''<html>
<head>
<link rel='stylesheet' href='{0}'/>
</head>
<body>
'''.format(css_filename)
html_footer = '''
</body>
'''
my_class = 'highlighter'

#
# code #
#
formatter = HtmlFormatter(linenos=True, cssclass=my_class)
f_css = open(css_filename, 'w')
f_css.write(formatter.get_style_defs('.' + my_class))
f_css.close()
code = open(sys.argv[0], 'r').read()
f_html = open(html_filename, 'w')
f_html.write(html_header)
highlight(code, PythonLexer(), formatter, f_html)
f_html.write(html_footer)
f_html.close()
