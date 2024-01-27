from mpmath import mp
# set the number of digits precision
mp.dps = 200
print(mp.quad(lambda x: mp.exp(-x**2), [-mp.inf, mp.inf]) ** 2)
