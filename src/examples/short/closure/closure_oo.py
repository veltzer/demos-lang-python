"""
This is an exapmle of how to use the closure feature to do some
oo work.
Notice:
- We treat the 'Person' function as a constructor.
- We call it with a capital first letter.
- We pass arguments to it needed to create the instance.
- In order to have lots of data in the closure we simply
store a flexible and big data structure in the closure (in this
case a dictionary).
- Because we want to return many methods and dont want tuples with
dozens of elements we return all method pointers in a dictionary as
well.
B This allows the user to call our methods by name instead of by
position in some returned tuple.
"""


def Person(name, age):
    data = {
        'name': name,
        'age': age,
    }

    def setName(iname):
        data['name'] = iname

    def getName():
        return data['name']

    def setAge(iage):
        data['age'] = iage

    def getAge():
        return data['age']

    def printMe():
        print('name', data['name'])
        print('age', data['age'])

    methods = {
        'setName': setName,
        'getName': getName,
        'setAge': setAge,
        'getAge': getAge,
        'printMe': printMe,
    }
    return methods


p1 = Person('Bilbo', 111)
p1['setName']('Sam')
p1['printMe']()
p2 = Person('Frodo', 33)
p2['setName']('Sauron')
p2['printMe']()
p1['printMe']()
