"""
Show how to import different modules and treat them as the same one.
"""

# type: ignore

import reimport_one

print(f"add(2,2) is {reimport_one.add(2, 2)}")

# pylint: disable=shadowed-import, wrong-import-position
# noqa: E402
import reimport_two as reimport_one  # type: ignore[no-redef]

print(f"add(2,2) is {reimport_one.add(2, 2)}")
