import contextlib
import os
import sys

outfile = "/tmp/out3.txt"


@contextlib.contextmanager
def redirect_output_to(filename):
    """Context manager to run with stdout redirected to filename.
    The file is opened for appending and closed when the block
    finishes.
    """
    old_stdout = sys.stdout
    new_stdout = sys.stdout = open(fname, "a")
    try:
        yield
    finally:
        sys.stdout = old_stdout
        new_stdout.close()


# Running this will destroy [outfile]!
# make sure file is empty
with open(outfile, "w"):
    pass
# test
print("This should output nothing:")
for name in ["Fred", "Barney"]:
    with redirect_output_to(outfile):
        print(f"Hello, {name}!")
print("The file now contains this:")
with open(outfile) as f:
    print(f.read())
# clean up
os.remove(outfile)
