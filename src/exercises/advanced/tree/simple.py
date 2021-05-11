"""
Print the current folder as a tree just like the tree(1) command line utility
"""

import os
import os.path

def print_tree(fullpath: str, filename: str, depth=0):
    print_str=" " * 3 * depth
    if os.path.isdir(fullpath):
        print(f"{print_str}{filename}")
        files = list(os.listdir(fullpath))
        for f in files:
            print_tree(os.path.join(fullpath, f), f, depth+1)
    if os.path.isfile(fullpath):
        print(f"{print_str}{filename}")


print_tree(".", ".")
