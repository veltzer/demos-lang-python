def swap_lists(l1, l2):
    for i in range(len(l1)):
        [l1[i], l2[i]] = [l2[i], l1[i]]


l1 = [2, 3, 4]
l2 = [8, 7, 6]
swap_lists(l1, l2)
print(l1)
print(l2)
