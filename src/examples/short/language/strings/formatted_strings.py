"""
This example shows how to use formatted strings in python.
"""

name = "Charlie"
age = 35

print(f"My name is {name} and Im {age} years old.")
# Output: My name is Charlie and Im 35 years old.

pi = 3.14159
print(f"The value of pi is approximately {pi:.2f}")
# Output: The value of pi is approximately 3.14

# This prints both the expression and its value, very useful
a = 5
b = 6
print(f"{a + b=}")
# Output: a+b=11
