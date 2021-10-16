"""
This is an example of how to use closure as a facade design pattern.
"""



def func_with_many_args(a, b, c, d, e, f, g):
    """
    A big function which has too many variables
    """
    print(a, b, c, d, e, f, g)


def wrap_it(a, c, d, e, g):
    def inner_func(b, f):
        return func_with_many_args(a, b, c, d, e, f, g)

    return inner_func


func_with_few_args = wrap_it('a_val', 'c_val', 'd_val', 'e_val', 'g_val')
func_with_few_args('b_val', 'f_val')
