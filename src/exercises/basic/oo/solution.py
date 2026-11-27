"""
Solution
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


people = []
id_to_person = {}
with open("people.csv") as stream:
    next(stream)  # skip the first line
    for raw_line in stream:
        line = raw_line.rstrip()  # remove the newline at the end
        values = line.split(",")
        # socialid, name, surname = line.split(",")  # noqa: ERA001  teaching: kept in the comment for the reader
        # p = Person(socialid, name, surname)  # noqa: ERA001  teaching: kept in the comment for the reader
        p = Person(*values)
        print(p)
        id_to_person[p.socialid] = p
        people.append(p)

# print(people)  # noqa: ERA001  teaching: kept in the comment for the reader
