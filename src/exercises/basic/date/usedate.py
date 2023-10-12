import date1  # type: ignore

baddate1 = date1.Date(37, 4, 5)
baddate2 = date1.Date(-5, 4, 5)
baddate3 = date1.Date(12, -1, 5)
baddate4 = date1.Date(12, 13, 5)
d1 = date1.Date(26, 2, 84)
d2 = date1.Date(12, 1, 88)

print(d1 > d2)
print(d1 < d2)

print(d1)
print(d2)
