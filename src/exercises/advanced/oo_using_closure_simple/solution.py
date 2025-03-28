"""
solution.py
"""


def make_a_stack():
    my_list = []

    def push(x):
        my_list.append(x)

    def pop():
        return my_list.pop()

    def show():
        print(my_list)

    return (push, pop, show)


def main():
    push_function, pop_function, show_function = make_a_stack()
    show_function()
    push_function(5)
    show_function()
    push_function(7)
    show_function()
    _ = pop_function()
    show_function()
    _ = pop_function()
    show_function()


if __name__ == "__main__":
    main()
