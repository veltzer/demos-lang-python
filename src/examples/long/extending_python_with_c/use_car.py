"""
this sys.path.append in the next section is needed since we didn"t
"properly" install the module to some standard python path location like /usr/share/python.
If we had this would not have been neccessary.
"""

import sys
sys.path.append(sys.argv[1])

# pylint: disable=wrong-import-position
import car  # noqa: E402
c = car.Car()
print(c)
c.printSelf()
c.setNumber(777)
print(c.getNumber())
