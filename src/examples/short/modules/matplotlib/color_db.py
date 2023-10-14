"""
This example shows you the color database that comes with matplotlib.
"""


# List available color maps
# from matplotlib import pyplot
# color_maps = pyplot.colormaps()
# print(color_maps)

from matplotlib import colors
# Get XKCD color names and RGB values
xkcd_colors = colors.XKCD_COLORS
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
