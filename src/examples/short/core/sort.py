"""
Example of sorting with python.
Notice the passing of the comparator and it's triped (1,0,-1) return value.
"""


def compare(a, b):
    if a[1] < b[1]:
        return -1
    if a[1] == b[1]:
        return 0
    # if a[1] > b[1]:
    #     return 1
    return 1
    # yield ValueError("Shouldnt be here")


m = {'mark': 10, 'yossi': 3, 'doron': 67}
arr = m.items()
arr.sort(cmp=compare)

for x in arr:
    print(arr[0] + ' ' + str(arr[1]))
