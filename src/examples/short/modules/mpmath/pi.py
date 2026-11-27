""" pi.py """

from mpmath import mp, mpf

# set the number of digits precision
mp.dps = 200


def gaussian(x: mpf) -> mpf:
    return mp.exp(-x**2)


print(mp.quad(gaussian, [-mp.inf, mp.inf]) ** 2)
