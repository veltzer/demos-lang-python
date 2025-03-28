"""
solution.py
"""


def Person(name, age):
    def data():
        pass

    def setName(name):
        data.__dict__["name"] = name

    def getName():
        return data.name

    def setAge(age):
        if age <= 0:
            raise ValueError("age error")
        data.__dict__["age"] = age

    def getAge():
        return data.age

    def printMe():
        print("name is ", data.name)
        print("age is ", data.age)

    data.setName = setName
    data.getName = getName
    data.setAge = setAge
    data.getAge = getAge
    data.printMe = printMe
    setName(name)
    setAge(age)
    return data


# usage...
p1 = Person("mark", 36)
p2 = Person("doron", 32)
print(p1.name)
p1.printMe()
p2.printMe()
p1.setName("foobar")
p1.setAge(74)
p1.printMe()
