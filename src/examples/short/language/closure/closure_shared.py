"""
This is an example of a shared closure. All three functions share the same closure or data.
"""


def create_funcs(number_list):
    def append_f(x):
        number_list.append(x)

    def print_f():
        print(number_list)

    def sum_f():
        return sum(number_list)

    return append_f, print_f, sum_f


(ap_f, pr_f, su_f) = create_funcs([1, 2, 3])
# lets start doing stuff with the three functions...
ap_f(4)
pr_f()
print(su_f())
ap_f(5)
pr_f()
print(su_f())
