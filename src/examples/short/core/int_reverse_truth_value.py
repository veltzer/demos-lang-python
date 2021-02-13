"""
An example of how to reverse the truth value of an integer in python
"""

for i in range(5):
    g=int(not bool(i))
    print(f"reverse of {i} is {g}")
