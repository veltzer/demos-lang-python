#! /usr/bin/python
# Python 3 version
# Calculate the height of a projectile.
# Ignores air resistance.

from math import pi, tan, cos
import matplotlib.pyplot as pyplot

# 1 Mile per Hour = 0.44704 Meters per Second.

g     = 9.81          # Acceleration due to gravity m/s squared.
v0    = 44            # The initial velocity m/s.
theta = 80 * pi/180   # The elevation angle in radians.
x     = 0.5           # The horizontal distance travelled.
y0    = 1             # The height of the barrel (m).

# Initial values for the graphic.
y = y0
x = 0.0
x_axis = []
y_axis = []

while y > 0:
    x = x + 0.1
    y = (y0 + x*tan(theta) - (g * x**2))/(2 * ((v0 * cos(theta))**2))

    print('x = {:.1f}m,     y = {:1f}m'.format(x, y))
    x_axis.append(x)
    y_axis.append(y)

# Graph.
pyplot.ylabel('Height m')
pyplot.xlabel('Distance m')

# Optional realism
pyplot.ylim(-1, max(max(x_axis), max(y_axis)))

pyplot.plot(x_axis, y_axis)
pyplot.show()


