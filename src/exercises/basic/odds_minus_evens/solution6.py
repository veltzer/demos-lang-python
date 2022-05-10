def odds_minus_evens(my_list):
    """ Returns the sum of odd numbers in the list minus the sum of evns """
    return sum(filter(lambda x: x % 2 != 0, my_list)) - sum(filter(lambda x: x % 2 == 0, my_list))
