"""
Dump information about the python pptx object that make up a slideshow

References:
- https://www.syncfusion.com/kb/8672/how-to-extract-text-from-a-powerpoint-presentation
- https://python-pptx.readthedocs.io/en/latest/#user-guide
"""
import sys

from pptx import Presentation
from pyvardump import dump_json

input_filename = sys.argv[1]

presentation = Presentation(input_filename)
slides = presentation.slides
# refs = set()  # noqa: ERA001  teaching: kept in the comment for the reader
for number, slide in enumerate(slides):
    print(f"slide {number}")
    dump_json(slide)
