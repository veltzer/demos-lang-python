#!/usr/bin/env python

class Person:
    def __init__(self, id, name, surname):
        self.id=id
        self.name=name
        self.surname=surname
    def __repr__(self):
        return f"repr <id {self.id}, name {self.name}, surname {self.surname}>"
    def __str__(self):
        return f"str <id {self.id}, name {self.name}, surname {self.surname}>"

class Car:
    def __init__(self, license, color, type):
        self.license=license
        self.color=color
        self.type=type
        self.owners = []
    def add_owner(self, owner):
        self.owners.append(owner)
    def __repr__(self):
        return f"repr <{license self.license}, color {self.color}, type {self.type}>"
    def __str__(self):
        return f"str <{license self.license}, color {self.color}, type {self.type}>"

people = []
id_to_person = {}
with open("people.csv", "rt") as stream:
    next(stream) # skip the first line
    for line in stream:
        line=line.rstrip() # remove the newline at the end
        values = line.split(",")
        p = Person(*values)
        print(p)
        id_to_person[p.id]=p
        people.append(p)

print(people)
