"""
An example showing how, to some extent closure can be seen as a replacement
for object oriented programming. The "Person" function below could
be seen as a sort of a constructor
"""


def Person(initial_name, initial_age):
    o = {
        "name": initial_name,
        "age": initial_age,
    }

    def getName():
        return o["name"]

    def setName(name):
        o["name"] = name

    def getAge():
        return o["age"]

    def setAge(age):
        o["age"] = age

    return {
        "getName": getName,
        "setName": setName,
        "getAge": getAge,
        "setAge": setAge,
    }


p = Person("Bilbo", 111)
p["setAge"](112)
print("age is", p["getAge"]())
p2 = Person("Frodo", 77)
p2["setAge"](78)
print("age is", p2["getAge"]())
