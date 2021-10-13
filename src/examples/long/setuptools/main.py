from pkgutil import walk_packages
import os
import setuptools

# this finds the config package too, no good
print(setuptools.find_packages())
# this is better but we need to know what to exclude and
# the right way to pass it!
print(setuptools.find_packages(exclude=["config.*", "config"]))


def find_packages_walk(path="", prefix=""):
    yield prefix
    prefix = prefix + "."
    for _, name, ispkg in walk_packages(path, prefix):
        if ispkg:
            yield name


# does not work, I don't know why...
print(list(find_packages_walk(path="my_pkg", prefix="my_pkg")))


def find_packages_os(path='.'):
    for root, _dirs, files in os.walk(path):
        if '__init__.py' in files:
            yield root.replace("/", ".")


# this is correct
print(list(find_packages_os(path="my_pkg")))
