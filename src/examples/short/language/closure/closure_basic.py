"""
This is a basic closure example.
"""


def make_adder(x):
    def adder(y):
        return x + y
    return adder


add5 = make_adder(5)
add3 = make_adder(3)

print(add5(7))  # 12
print(add5(12))  # 17
print(add3(5))  # 8
print(add3(2))  # 5
