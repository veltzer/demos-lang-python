"""
This is an example of a shared closure. The three functions here share the x
variable.

- note that in this example the closure is just one element 'x' which is
the parameter of the function 'make_mul_add_print'
- this means that we cannot change it. Why? because it is a primitive.
If we try to change it in another function that we add,say f_set,
then the statement 'x=...' will be taken by python to mean the declaration
of another *** local *** variable 'x'.
"""


def make_mul_add_print(x):
    def f_mul(y):
        return x * y

    def f_add(y):
        return x + y

    def f_print():
        print(x)

    return f_mul, f_add, f_print


(func_mul3, func_add3, func_print3) = make_mult_add_print(3)
(func_mul5, func_add5, func_print5) = make_mult_add_print(5)

print('the 3 family of functions')
func_print3()
print(func_mul3(4))
print(func_add3(4))
print('the 5 family of functions')
func_print5()
print(func_mul5(6))
print(func_add5(6))

# lets see if the closures of the functions returned together are the same...
if func_mul3.__closure__ is func_add3.__closure__ is func_set3.__closure__:
    print('yes,the three functions have the exact same closure')
# lets see if different invocations actually created different closures...
if func_mul3.__closure__ is not func_mul5.__closure__:
    print(
        'yes,the closure object of the 3 family is not the closure object of the 5 family')
# here is how we can get to the closure object from the outside:
print('the closure for the 3 family of functions holds the value',
      func_add3.__closure__[0].cell_contents)
try:
    func_add3.__closure__[0].cell_contents = 8
except AttributeError as e:
    print(
        'no,I cannot set the closure data from the outside. It is indeed \'private\'...')
    print('the error we got is', e)
