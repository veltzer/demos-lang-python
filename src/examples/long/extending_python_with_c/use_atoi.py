"""
the sys.path.append in the next section is needed since we didn"t "properly"
install the module to /usr/share/python.
If we had done this this would not have been neccessary.
"""

import sys
# noinspection PyPep8
# pylint: disable=import-error
import atoi  # noqa: E402


sys.path.append("build/lib.linux-i686-2.7")
print(atoi.atoi("-7.6"))
