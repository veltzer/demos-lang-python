"""
Print the current folder as a tree just like the tree(1) command line utility
"""

import os
import os.path

def print_tree(fullpath: str, filename: str, print_str_under="", print_str_continue=""):
    if os.path.isdir(fullpath):
        print(f"{print_str_under}{filename}")
        files = list(os.listdir(fullpath))
        for i, f in enumerate(files):
            if i==len(files)-1:
                cont="└──"
            else:
                cont="├──"
            flow_cont="│  "
            print_tree(os.path.join(fullpath, f), f, print_str_continue+cont, print_str_continue+flow_cont)
    if os.path.isfile(fullpath):
        print(f"{print_str_continue}{filename}")


print_tree(".", ".")
