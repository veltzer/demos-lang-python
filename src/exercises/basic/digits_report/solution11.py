found = True
input_string = None
while found:
    input_string = input("Please give me some digits... \n")
    found = False
    for character in input_string:
        if ord(character) < ord("0") or ord(character) > ord("9"):
            # we have a non digit!
            print("Error, you gave me non digits")
            found = True
            break
print("starting real work on", input_string)
assert input_string is not None
# this is the easy solution...
for digit in range(10):
    print(f"digit {digit} appears {input_string.count(str(digit))} times")
# this is the right one...
counters = [0] * 10
for digit1 in input_string:
    counters[int(digit1)] += 1
for digit, count in enumerate(counters):
    print("digit", digit, " appears", count, " times")
