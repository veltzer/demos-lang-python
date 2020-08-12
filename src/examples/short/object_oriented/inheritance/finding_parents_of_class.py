"""
This example shows how to find the parents of a class in python.

NOTES:
- CLASS.__base__ only gives you the first parents. Use __bases__ to get them all.

References:
- https://stackoverflow.com/questions/2611892/get-class-parents
"""


class A:
    pass


class B(A):
    pass


class C:
    pass


class D(B, C):
    pass


print(A.__base__, A.__bases__)
print(B.__base__, B.__bases__)
print(C.__base__, C.__bases__)
print(D.__base__, D.__bases__)
