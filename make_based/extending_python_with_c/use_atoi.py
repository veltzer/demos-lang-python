"""
the sys.path.append in the next section is needed since we didn"t "properly"
install the module to /usr/share/python.
If we had done this this would not have been neccessary.
"""

import sys
sys.path.append(sys.argv[1])
# pylint: disable=wrong-import-position,import-error
import atoi  # type: ignore # noqa: E402


# the whole path is: python "str" -> C string (char*) -> calls c "atoi" - > C int (64 bit, singed) -> Python "int"
r = atoi.atoi("-7.6")
print(type(r))
print(r)
