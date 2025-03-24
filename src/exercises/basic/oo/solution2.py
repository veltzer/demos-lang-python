"""
Solution2
"""

class Person:
    def __init__(self, socialid, name, surname):
        self.socialid = socialid
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"repr <socialid {self.socialid}, name {self.name}, surname {self.surname}>"

    def __str__(self):
        return f"str <socialid {self.socialid}, name {self.name}, surname {self.surname}>"


class Car:
    def __init__(self, licenseid, color, cartype):
        self.licenseid = licenseid
        self.color = color
        self.cartype = cartype
        self.owners = []

    def add_owner(self, owner):
        self.owners.append(owner)

    def __repr__(self):
        return f"repr <licenseid {self.licenseid}, color {self.color}, cartype {self.cartype}>"

    def __str__(self):
        return f"str <licenseid {self.licenseid}, color {self.color}, cartype {self.cartype}>"


people = []
id_to_person = {}
with open("people.csv", "rt") as stream:
    next(stream)  # skip the first line
    for line in stream:
        line = line.rstrip()  # remove the newline at the end
        values = line.split(",")
        p = Person(*values)
        print(p)
        id_to_person[p.socialid] = p
        people.append(p)
print(people)
