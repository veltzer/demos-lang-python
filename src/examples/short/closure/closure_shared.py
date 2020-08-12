"""
This is an example of a shared closure. All three functions share the same closure or data.
"""


def create_funcs(l):
    def append_f(x):
        l.append(x)

    def print_f():
        print(l)

    def sum_f():
        return sum(l)

    return append_f, print_f, sum_f


(ap_f, pr_f, su_f) = create_funcs([1, 2, 3])
# lets start doing stuff with the three functions...
ap_f(4)
pr_f()
print(su_f())
ap_f(5)
pr_f()
print(su_f())
