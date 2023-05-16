s = input("Please enter a line of digits: ")
if not s.isdigit():
    print("Error: only digits allowed!")
else:
    for digit in range(10):
        print(digit, "appears", s.count(str(digit)), "times")
