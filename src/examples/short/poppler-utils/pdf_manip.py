"""
A script to separate the a pdf to separate slides...
"""

import os.path
import subprocess

subprocess.check_output([
    'pdfseparate',
    'file.pdf',
    'page-%d.pdf',
])
slide = 1
till = 166
width = 283 - 90
height = 498 - 340
margin_x = 50  # ?!? guessing again
for x in range(1, till):
    filename = f"page-{x}.pdf"
    if not os.path.isfile(filename):
        raise ValueError(f"no such file {filename}")
    slide_name = f"slide-{slide:03d}.pdf"
    slide += 1
    start_x = 90
    start_y = 340
    to_x = start_x + width
    to_y = start_y + height
    area = f"{start_x} {start_y} {to_x} {to_y}"
    print(f"area is {area}")
    subprocess.check_output([
        'pdfcrop',
        filename,
        '--bbox',
        area,
        slide_name,
    ])
    start_x += width + margin_x
    to_x = start_x + width
    to_y = start_y + height
    slide_name = f"slide-{slide:03}.pdf"
    slide += 1
    area = f"{start_x} {start_y} {to_x} {to_y}"
    print(f"frmt is {area}")
    subprocess.check_output([
        'pdfcrop',
        filename,
        '--bbox',
        area,
        slide_name,
    ])
    start_x += width + margin_x
    to_x = start_x + width
    to_y = start_y + height
    slide_name = f"slide-{slide:03d}.pdf"
    slide += 1
    area = f"{start_x} {start_y} {to_x} {to_y}"
    print(f"frmt is {area}")
    subprocess.check_output([
        'pdfcrop',
        filename,
        '--bbox',
        area,
        slide_name,
    ])
