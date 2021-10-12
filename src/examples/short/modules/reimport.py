"""
Show how to import different modules and treat them as the same one.
"""

import reimport_one

print('add(2,2) is', reimport_one.add(2, 2))

import reimport_two as reimport_one  # noqa: E402

print('add(2,2) is', reimport_one.add(2, 2))
