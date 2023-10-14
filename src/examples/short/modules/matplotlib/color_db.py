"""
This example shows you the color database that comes with matplotlib.
"""

from matplotlib import pyplot
from matplotlib import colors

color_maps = pyplot.colormaps()
for color_map in color_maps:
    print(color_map)

colors_dbs = [
    colors.XKCD_COLORS,
    colors.TABLEAU_COLORS,
    colors.BASE_COLORS,
    colors.CSS4_COLORS,
]

for color_db in colors_dbs:
    # print(dir(color_db))
    for name, rgb in color_db.items():
        print(f"{name}: {rgb}")
