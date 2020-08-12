"""
This is to show that cloures can be more than one layer deep.
Here y is a local variable, x is in the closure and z is in
the closure of the closure.
"""

z = 2


def make_adder(x):
    def adder(y):
        return x + y + z

    return adder


add5 = make_adder(5)
add3 = make_adder(3)

print(add5(7))  # 14
print(add5(12))  # 19
print(add3(5))  # 10
print(add3(2))  # 7
