from scipy import integrate

# Function to integrate
def f(x):
    return x**2

# Integration bounds  
lower = 0  
upper = 2

# Number of subintervals 
N = 1000   

# Integration step size
dx = (upper - lower) / N

# Initialize result  
result = 0

# Integrate using Riemann sum   
for i in range(N):
    x = lower + i*dx
    result += f(x) * dx

print(result)
