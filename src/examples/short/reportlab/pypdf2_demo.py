"""
Make some simple multi-page pdf files.

References:
https://github.com/mstamy2/PyPDF2/raw/master/Sample_Code/makesimple.py
"""

import reportlab.pdfgen.canvas

point = 1
inch = 72

TEXT = '''%s    page %d of %d a wonderful file created with python'''


def make_pdf_file(output_filename, np):
    # title = output_filename
    c = reportlab.pdfgen.canvas.Canvas(output_filename, pagesize=(8.5 * inch, 11 * inch))
    c.setStrokeColorRGB(0, 0, 0)
    c.setFillColorRGB(0, 0, 0)
    c.setFont("Helvetica", 12 * point)
    for pn in range(1, np + 1):
        v = 10 * inch
        for sub_line in (TEXT % (output_filename, pn, np)).split('\n'):
            c.drawString(1 * inch, v, sub_line)
            v -= 12 * point
        c.showPage()
    c.save()


page_numbers = [5, 11, 17]
for i, page_number in enumerate(page_numbers):
    filename = f"/tmp/simple{i}.pdf"
    make_pdf_file(filename, page_number)
    print("Wrote", filename)
