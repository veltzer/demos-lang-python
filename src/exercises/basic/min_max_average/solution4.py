def min_max_avg(number_list):
    min_value = number_list[0]
    max_value = number_list[0]
    sum_value = number_list[0]
    for i in range(1, len(number_list)):
        x = number_list[i]
        min_value = min(min_value, x)
        max_value = max(max_value, x)
        sum_value += x
    return min_value, max_value, sum_value / len(number_list)


print(min_max_avg(range(0, 100000)))
