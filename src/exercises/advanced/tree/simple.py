"""
Print the current folder as a tree just like the tree(1) command line utility
"""

import os
import os.path

def print_tree(fullpath: str, filename: str, depth=0):
    print_str=" " * 3 * depth
    print(f"{print_str}{filename}")
    if os.path.isdir(fullpath):
        for f in os.listdir(fullpath):
            print_tree(os.path.join(fullpath, f), f, depth+1)

print_tree(".", ".", 0)
