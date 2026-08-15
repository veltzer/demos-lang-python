"""
Simple demo of weasy print
"""

from weasyprint import CSS, HTML

# 1. Your HTML content
html_content = """
<html>
  <body>
    <h1>My First WeasyPrint PDF</h1>
    <p>This document was generated on a Friday night in Holon!</p>
  </body>
</html>
"""

# 2. Your CSS for styling
css_style = """
body {
  font-family: sans-serif;
}
h1 {
  color: #369; /* A nice blue */
}
"""

# 3. Generate the PDF
html = HTML(string=html_content)
css = CSS(string=css_style)
html.write_pdf(
    "/tmp/output.pdf",
    stylesheets=[css]
)

print("PDF 'my_document.pdf' created successfully.")
