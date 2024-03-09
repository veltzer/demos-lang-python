import sympy as sym

x = sym.Symbol("x")
y = sym.Symbol("y")

expression = 3 * x**2 + 2 * x * y + y**2

print(expression)

# Take the derivative with respect to x
derivative = sym.diff(expression, x)

print(derivative)

# Substitute a value for y
derivative_sub = derivative.subs({y:5})

print(derivative_sub)

# Solve the derivative equal to 0
solution = sym.solve(derivative_sub, x)

print(solution)
