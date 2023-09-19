"""
the sys.path.append in the next section is needed since we didn"t "properly"
install the module to /usr/share/python.
If we had done this this would not have been neccessary.
"""

import sys
sys.path.append(sys.argv[1])
# pylint: disable=wrong-import-position
import atoi  # noqa: E402


print(atoi.atoi("-7.6"))
