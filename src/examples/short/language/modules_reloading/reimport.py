"""
Show how to import different modules and treat them as the same one.
"""

import reimport_one  #  type: ignore[import-not-found]

print(f"add(2,2) is {reimport_one.add(2, 2)}")

# pylint: disable=shadowed-import, wrong-import-position
import reimport_two as reimport_one  # noqa: E402  teaching: re-import under the same name

print(f"add(2,2) is {reimport_one.add(2, 2)}")
