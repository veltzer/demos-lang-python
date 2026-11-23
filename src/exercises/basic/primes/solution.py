"""
Solution
"""

nums: list[int | None] = list(range(100))
d = 2
while d <= 10:
    for i, x in enumerate(nums):
        if x is not None and x % d == 0 and x != d:
            nums[i] = None
    d += 1
print(nums)
