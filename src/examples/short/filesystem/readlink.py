"""
This is an example of how to read a symbolic link in python.
the API is os.readlink()
Notice that if you read the target of the symlink it is not enough
to find the file it is pointing too. If what you read is an absolute
path then this is fine. If it is relative you must interpret it relative
to the folder of where the *symlink* is, not relative to your current
working directory. See the the code below.

Another issue you need to take care of is to make sure that the symlink
does not point to another symlink, in that case you need to redo the whole
thing once again...

It turns out that os.path.realpath does all of this iterative resolution
of a symbolic link but doesn't care if any of the symlinks in the process
do not point to a real file (in that case it just stops). See the shorter
version in the code below.
"""

import os
import os.path


def find_link_target(link):
    assert os.path.islink(link)
    link_folder = os.path.dirname(link)
    link_target = os.readlink(link)
    if not os.path.isabs(link_target):
        real_link_target = os.path.join(link_folder, link_target)
    # fix the path so that it doesn't contain superfluous parts like ../ etc
    real_link_target = os.path.abspath(real_link_target)
    return real_link_target


def find_link_target_rec(link):
    while os.path.islink(link):
        link = find_link_target(link)
    return link


def find_link_target_better(link):
    assert os.path.islink(link)
    real = os.path.realpath(link)
    assert os.path.exists(real)
    return real


'''
this is a file name which is a symbolic name on most linux
systems
'''
link = '/tmp/foo'
link = '/etc/resolv.conf'
real_link_target = find_link_target_rec(link)
assert os.path.exists(real_link_target) and not os.path.islink(real_link_target)

print(os.path.realpath(link))
print(find_link_target_better(link))
