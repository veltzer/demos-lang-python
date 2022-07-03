from typing import List, Optional

nums: List[Optional[int]] = list(range(0, 100))
for d in range(2, 11):
    if nums[d] is not None:
        for x in range(d + d, 100, d):
            nums[x] = None
prims = filter(lambda x: x is not None, nums)
print(prims)
