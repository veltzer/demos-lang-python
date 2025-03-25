"""
print_profile_results.py
"""

import pstats

p = pstats.Stats("/tmp/profile_results")
p.sort_stats("cumulative").print_stats(20)
# p.strip_dirs().sort_stats(-1).print_stats()
