class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


p = Person("yossi", 24)

t = getattr(p, "get_name")
print(t)
print(t())
u = Person.get_name
print(u)
print(u(p))

while True:
    method_name = input("give me a method name to call... ")
    print(getattr(p, method_name)())
