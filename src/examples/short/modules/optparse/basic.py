"""
A demo for the optparse module.
This is not the best module for argument parsing in python.
If you want a better module use argparse (see demo_argparse.py)

try this command to check it out:
./demo_optparse.py --toplevel=foobar

References:
"""

# pylint: disable=deprecated-module
import optparse

parser = optparse.OptionParser(
    description=__doc__,
    usage="%prog [options]",
)
parser.add_option("", "--mail-folder", dest="mail-folder",
                  default="~/Mail", help="Folder where mail is. [default: %default]")
parser.add_option("", "--debug", action="store_true", dest="debug",
                  default=False, help="do you want to debug the script? [default: %default]")
parser.add_option("", "--exit", action="store_true", dest="exit",
                  default=False, help="exit after debug? [default: %default]")
parser.add_option("", "--no-progress", action="store_true", dest="no-progress",
                  default=False, help="dont report progress [default: %default]")
parser.add_option(
    "", "--toplevel", dest="toplevel", default="default for toplevel",
    help="toplevel tag for importing [default: %default]")
(options, args) = parser.parse_args()

print(options)
print(args)
