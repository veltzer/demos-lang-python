"""
This example shows how to use the apt package from python.
This shows how to install packages.

You need to run this as root

Why would you want to install packages this way? It's a lot more efficient
and less error prone than using apt-get(1) on the command line.
Check how long it take you to run apt-get(1) to install a bunch of packages
already installed and how long it takes this script to do the same work...

References:
http://stackoverflow.com/questions/17537390/how-to-install-a-package-using-the-python-apt-api
"""

import os

import apt.cache

pkg_names = [
    'templar',
]
do_update = False

if os.geteuid() == 0:
    print('you are root, that is good, proceeding...')
else:
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")

cache = apt.cache.Cache()
if do_update:
    print('doing update')
    cache.update()

need_commit = False
for pkg_name in pkg_names:
    pkg = cache[pkg_name]
    if pkg.is_installed:
        print('package [{pkg_name}] already installed'.format(pkg_name=pkg_name))
    else:
        pkg.mark_install()
        need_commit = True

# this actually installs
if need_commit:
    print('doing commit')
    cache.commit()
