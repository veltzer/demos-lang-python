"""
solution.py
"""


def Person(name, age):
    def data():
        pass

    def setName(name):
        data.__dict__["name"] = name

    def getName():
        return data.name  # pyrefly: ignore[missing-attribute]

    def setAge(age):
        if age <= 0:
            raise ValueError("age error")
        data.__dict__["age"] = age

    def getAge():
        return data.age  # pyrefly: ignore[missing-attribute]

    def printMe():
        print("name is ", data.name)  # pyrefly: ignore[missing-attribute]
        print("age is ", data.age)  # pyrefly: ignore[missing-attribute]

    data.setName = setName  # pyrefly: ignore[missing-attribute]
    data.getName = getName  # pyrefly: ignore[missing-attribute]
    data.setAge = setAge  # pyrefly: ignore[missing-attribute]
    data.getAge = getAge  # pyrefly: ignore[missing-attribute]
    data.printMe = printMe  # pyrefly: ignore[missing-attribute]
    setName(name)
    setAge(age)
    return data


# usage...
p1 = Person("mark", 36)
p2 = Person("doron", 32)
print(p1.name)  # pyrefly: ignore[missing-attribute]
p1.printMe()  # pyrefly: ignore[missing-attribute]
p2.printMe()  # pyrefly: ignore[missing-attribute]
p1.setName("foobar")  # pyrefly: ignore[missing-attribute]
p1.setAge(74)  # pyrefly: ignore[missing-attribute]
p1.printMe()  # pyrefly: ignore[missing-attribute]
