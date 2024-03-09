def min_max_avg(num_list):
    min_value = num_list[0]
    max_value = num_list[0]
    sum_value = num_list[0]
    for x in num_list[1:]:
        min_value = min(min_value, x)
        max_value = max(max_value, x)
        sum_value += x
    return min_value, max_value, sum_value / len(num_list)


print(min_max_avg(range(0, 100000)))
