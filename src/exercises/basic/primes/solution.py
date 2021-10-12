nums = list(range(0, 100))
d = 2
while d <= 10:
    i = 0
    for x in nums:
        if x is not None and x % d == 0 and x != d:
            nums[i] = None
        i += 1
    d += 1
print(nums)
