"""
Thjis is a simple example of how to make an svg file using
the `svgwrite` module
"""

from svgwrite import Drawing


dwg = Drawing("/tmp/test.svg", size=("200px", "200px"))
dwg.add(dwg.line((0, 0), (100, 100), stroke="black"))
dwg.save()
