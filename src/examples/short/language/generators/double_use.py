def give_me_some_data():
    yield 7
    yield -14
    yield True


for x in give_me_some_data():
    print("outer loop", x)
    for y in give_me_some_data():
        print("inner loop", y)
