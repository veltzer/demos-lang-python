def odds_minus_evens(number_list):
    """ Returns the sum of odd numbers in the list minus the sum of evns """
    sum_value = 0
    for x in number_list:
        if x % 2 == 0:
            sum_value -= x
        else:
            sum_value += x
    return sum_value


print(odds_minus_evens(range(10)))
