#!/usr/bin/env python

class Person:
    def __init__(self, socialid, name, surname):
        self.socialid = socialid
        self.name = name
        self.surname = surname
        self.cars = []

    def __repr__(self):
        return f"<socialid {self.socialid}, name {self.name}, surname {self.surname}>"

    def __str__(self):
        return self.__repr__()

    def add_car(self, c):
        self.cars.append(c)


class Car:
    def __init__(self, licenseid, color, cartype):
        self.licenseid = licenseid
        self.color = color
        self.cartype = cartype
        self.owners = []

    def add_owner(self, owner):
        self.owners.append(owner)

    def __repr__(self):
        return f"<licenseid {self.licenseid}, color {self.color}, cartype {self.cartype}>"

    def __str__(self):
        return self.__repr__()


def main():
    people = []
    id_to_person = {}
    with open("people.csv", "rt") as stream:
        next(stream)  # skip the first line
        for line in stream:
            line = line.rstrip()  # remove the newline at the end
            values = line.split(",")
            p = Person(*values)
            id_to_person[p.socialid] = p
            people.append(p)
    # print(people)

    cars = []
    license_to_car = {}
    with open("cars.csv", "rt") as stream:
        next(stream)  # skip the first line
        for line in stream:
            line = line.rstrip()  # remove the newline at the end
            values = line.split(",")
            c = Car(values[0], values[1], values[3])
            license_to_car[c.licenseid] = c
            cars.append(c)
            # lets handle the owners field
            owners = values[2].split("-")
            for owner in owners:
                p = id_to_person[owner]
                p.add_car(c)
                c.add_owner(p)
    print(cars)


if __name__ == "__main__":
    main()
