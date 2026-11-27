"""
Solution3
"""


class Person:
    def __init__(self, socialid: str, name: str, surname: str) -> None:
        self.socialid = socialid
        self.name = name
        self.surname = surname
        self.cars = []

    def __repr__(self) -> str:
        return f"<socialid {self.socialid}, name {self.name}, surname {self.surname}>"

    def __str__(self) -> str:
        return self.__repr__()

    def add_car(self, c: Car) -> None:
        self.cars.append(c)


class Car:
    def __init__(self, licenseid: str, color: str, cartype: str) -> None:
        self.licenseid = licenseid
        self.color = color
        self.cartype = cartype
        self.owners = []

    def add_owner(self, owner: Person) -> None:
        self.owners.append(owner)

    def __repr__(self) -> str:
        return f"<licenseid {self.licenseid}, color {self.color}, cartype {self.cartype} owners {self.owners}>"

    def __str__(self) -> str:
        return self.__repr__()


def main() -> None:
    people = []
    id_to_person = {}
    with open("people.csv") as stream:
        next(stream)  # skip the first line
        for raw_line in stream:
            line = raw_line.rstrip()  # remove the newline at the end
            values = line.split(",")
            p = Person(*values)
            id_to_person[p.socialid] = p
            people.append(p)
    # print(people)  # noqa: ERA001  teaching: kept in the comment for the reader

    cars = []
    license_to_car = {}
    with open("cars.csv") as stream:
        next(stream)  # skip the first line
        for raw_line in stream:
            line = raw_line.rstrip()  # remove the newline at the end
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
    for car in cars:
        print(car)


if __name__ == "__main__":
    main()
