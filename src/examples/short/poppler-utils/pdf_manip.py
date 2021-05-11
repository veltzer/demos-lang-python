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
    filename = 'page-{x}.pdf'.format(x=x)
    if not os.path.isfile(filename):
        raise ValueError('no such file ' + filename)
    slide_name = 'slide-%03d.pdf' % slide
    slide += 1
    start_x = 90
    start_y = 340
    to_x = start_x + width
    to_y = start_y + height
    area = '{start_x} {start_y} {to_x} {to_y}'.format(
        start_x=start_x,
        start_y=start_y,
        to_x=to_x,
        to_y=to_y,
    )
    print('area is', area)
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
    slide_name = 'slide-%03d.pdf' % slide
    slide += 1
    area = '{start_x} {start_y} {to_x} {to_y}'.format(
        start_x=start_x,
        start_y=start_y,
        to_x=to_x,
        to_y=to_y,
    )
    print('frmt is', area)
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
    slide_name = 'slide-%03d.pdf' % slide
    slide += 1
    area = '{start_x} {start_y} {to_x} {to_y}'.format(
        start_x=start_x,
        start_y=start_y,
        to_x=to_x,
        to_y=to_y,
    )
    print('frmt is', area)
    subprocess.check_output([
        'pdfcrop',
        filename,
        '--bbox',
        area,
        slide_name,
    ])
