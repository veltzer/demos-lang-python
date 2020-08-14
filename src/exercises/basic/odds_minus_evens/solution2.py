def odds_minus_evens(number_list):
    count = 0
    for x in number_list:
        if x % 2 == 0:
            count -= x
        else:
            count += x
    return count


print(odds_minus_evens(range(2, 6)))
