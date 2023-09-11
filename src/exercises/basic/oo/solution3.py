#!/usr/bin/env python

class Person:
    def __init__(self, id, name, surname):
        self.id=id
        self.name=name
        self.surname=surname
        self.cars = []
    def __repr__(self):
        return f"<id {self.id}, name {self.name}, surname {self.surname}>"
    def __str__(self):
        self.__repr__()
    def add_car(self, c: Car):
        assert isinstance(c, Car)
        self.cars.append(c)

class Car:
    def __init__(self, license, color, type):
        self.license=license
        self.color=color
        self.type=type
        self.owners = []
    def add_owner(self, owner):
        self.owners.append(owner)
    def __repr__(self):
        return f"<license {self.license}, color {self.color}, type {self.type}>"
    def __str__(self):
        self.__repr__()

people = []
id_to_person = {}
with open("people.csv", "rt") as stream:
    next(stream) # skip the first line
    for line in stream:
        line=line.rstrip() # remove the newline at the end
        values = line.split(",")
        p = Person(*values)
        id_to_person[p.id]=p
        people.append(p)
# print(people)

cars = []
license_to_car = {}
with open("cars.csv", "rt") as stream:
    next(stream) # skip the first line
    for line in stream:
        line=line.rstrip() # remove the newline at the end
        values = line.split(",")
        c = Car(values[0], values[1], values[3])
        license_to_car[c.license]=c
        cars.append(c)
        # lets handle the owners field
        owners = values[2].split("-")
        for owner in owners:
            p = id_to_person[owner]
            p.add_car(c)
            c.add_owner(p)
print(cars)