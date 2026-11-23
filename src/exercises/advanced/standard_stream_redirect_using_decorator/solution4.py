"""
solution4.py
"""

import sys


def with_output_to_outfile(filename):
    def creator(f):
        def decorated_f(*args, **kw):
            old_stdout = sys.stdout
            with open(filename, "a") as new_stdout:
                sys.stdout = new_stdout
                try:
                    return f(*args, **kw)
                finally:
                    sys.stdout = old_stdout
        return decorated_f
    return creator


@with_output_to_outfile(filename="/tmp/foo.txt")
def hello(name):
    print(f"Hello, {name}!")


def main():
    print("You should not see Fred or Barney on your screen")
    hello("Fred")
    hello("Barney")
    print("You should now see this")


if __name__ == "__main__":
    main()
