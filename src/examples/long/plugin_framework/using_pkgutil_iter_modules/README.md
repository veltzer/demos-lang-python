# Using `pkgutil` to iterate modules

The advantages of this approach
* only uses `pkgutil` which is built-in in python and has been for a long time.
* very simple to implement.

The disadvantages of this approach:
* not recursive.
* still needs to add auto class detection if one wants this.
