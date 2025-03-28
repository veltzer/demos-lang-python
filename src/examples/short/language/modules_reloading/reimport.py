"""
Show how to import different modules and treat them as the same one.
"""

# type: ignore

import reimport_one

print(f"add(2,2) is {reimport_one.add(2, 2)}")

# pylint: disable=shadowed-import, wrong-import-position
import reimport_two as reimport_one  # noqa: E402

print(f"add(2,2) is {reimport_one.add(2, 2)}")
