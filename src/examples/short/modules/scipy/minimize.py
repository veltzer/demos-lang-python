"""
minimize.py
"""

from scipy import integrate, optimize


# Function to integrate
def f(z):
    return z**2


# Integral bounds
lower = 0
upper = 2

# Integrate
result, error = integrate.quad(f, lower, upper)
print(result)

# Minimize f(x) = x^2 - 4x + 4
res = optimize.minimize(lambda x: (x**2 - 4 * x + 4), 0)
print(res.x)
