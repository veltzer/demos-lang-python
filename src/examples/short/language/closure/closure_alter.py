"""
This is an example that shows that we can change the closure if
it made up of non primitive data.

Here are the ways to do it:
- We may return a "closure altering" function which then can be
used to change the closure.
- We may return a function that returns pointers to the data in
the closure. If these are data structures (lists,dictionaries
or sets) then they will be returned by reference and thus we
will be able to change them from the outside. If these are object
then they will also be returned by reference and again we could
alter them from the outside.
- A third way would be to use the __closure__ attribute and access
the data through that.
"""


def make_funcs(number_list):
    def func_max():
        current_max = 0
        for x in number_list:
            current_max = max(current_max, x)
        return current_max

    def func_min():
        current_min = 10000
        for x in number_list:
            current_min = min(current_min, x)
        return current_min

    def func_set(index, val):
        number_list[index] = val

    def func_int():
        return number_list

    return func_max, func_min, func_set, func_int


(f_max, f_min, f_set, f_int) = make_funcs([1, 2, 3, 4])
# notice that we do not have a direct pointer to the list
# in question which was passed to the closure. We now must
# alter the list via the mechanisms described above.

# first lets output the initial state
print("f_max is", f_max())
print("f_min is", f_min())

print("""
lets use the first method mentioned above. lets use the f_set
function to alter the closure
""")
f_set(3, 5)
f_set(2, 0)
print("f_max is", f_max())
print("f_min is", f_min())

print("""
lets use the second method mentioned above. returning the internals
of the closure using a closure function...
""")
f_int()[3] = 6
f_int()[2] = -1
print("f_max is", f_max())
print("f_min is", f_min())

print("""
lets use the third method mentioned above. the __closure__ property.
""")
f_max.__closure__[0].cell_contents[3] = 7
f_max.__closure__[0].cell_contents[2] = -2
print("f_max is", f_max())
print("f_min is", f_min())

# after we do this then the list will be garbage collected...
f_max = None
f_min = None
f_set = None
f_int = None
