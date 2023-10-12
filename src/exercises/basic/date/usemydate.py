import mydate  # type: ignore

for i in mydate.months_name:
    print("month is ", i)
    print("this month has", mydate.get_num_of_days_in_month(i), "days")
    print("this month is followed by", mydate.get_following_month(i))

for year in range(2000, 2010):
    if mydate.is_leap_year(year):
        print("year", year, "is a leap year")
