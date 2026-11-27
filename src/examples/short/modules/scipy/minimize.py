"""
minimize.py
"""

from typing import TYPE_CHECKING

from scipy import integrate, optimize

if TYPE_CHECKING:
    import numpy as np


# Function to integrate
def f(z: float):
    return z**2


# Integral bounds
lower = 0
upper = 2

# Integrate
result, error = integrate.quad(f, lower, upper)
print(result)

# Minimize f(x) = x^2 - 4x + 4
def parabola(x: np.ndarray) -> np.ndarray:
    return x**2 - 4 * x + 4


res = optimize.minimize(parabola, 0)
print(res.x)
