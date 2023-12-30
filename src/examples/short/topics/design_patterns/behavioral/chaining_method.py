from __future__ import annotations
from contextlib import redirect_stdout
import io


class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    def do_action(self, action: Action) -> Action:
        print(self.name, action.name, end=" ")
        return action


class Action:
    def __init__(self, name: str) -> None:
        self.name = name

    def amount(self, val: str) -> Action:
        print(val, end=" ")
        return self

    def stop(self) -> None:
        print("then stop")


CORRECT_OUTPUT = """\
Jack move 5m then stop
"""


def main():
    move = Action("move")
    person = Person("Jack")
    with redirect_stdout(io.StringIO()) as output:
        person.do_action(move).amount("5m").stop()
    assert output.getvalue() == CORRECT_OUTPUT


if __name__ == "__main__":
    main()
