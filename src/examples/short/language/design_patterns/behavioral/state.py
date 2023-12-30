"""
Implementation of the state pattern

http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/

*TL;DR
Implements state as a derived class of the state pattern interface.
Implements state transitions by invoking methods from the pattern's superclass.
"""

from __future__ import annotations
from typing import List
import abc
from contextlib import redirect_stdout
import io


class State:
    __metaclass__ = abc.ABCMeta
    """Base state. Put shared state and functionality here"""

    def __init__(self, name: str, stations: List[str], radio: Radio) -> None:
        self.radio = radio
        self.stations = stations
        self.pos = 0
        self.name = name

    def scan(self) -> None:
        """Scan the dial to the next station"""
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print(f"Scanning... Station is {self.stations[self.pos]} {self.name}")

    @abc.abstractmethod
    def toggle_amfm(self) -> None:
        pass


class AmState(State):
    def __init__(self, radio: Radio) -> None:
        super().__init__(name="AM", stations=["1250", "1380", "1510"], radio=radio)

    def toggle_amfm(self) -> None:
        print("Switching to FM")
        self.radio.state = self.radio.fmstate


class FmState(State):
    def __init__(self, radio: Radio) -> None:
        super().__init__(name="FM", stations=["81.3", "89.1", "103.9"], radio=radio)

    def toggle_amfm(self) -> None:
        print("Switching to AM")
        self.radio.state = self.radio.amstate


class Radio:
    """A radio. It has a scan button, and an AM/FM toggle switch."""

    def __init__(self) -> None:
        """We have an AM state and an FM state"""
        self.amstate = AmState(self)
        self.fmstate = FmState(self)
        self.state = self.amstate

    def toggle_amfm(self) -> None:
        self.state.toggle_amfm()

    def scan(self) -> None:
        self.state.scan()


CORRECT_OUTPUT = """\
Scanning... Station is 1380 AM
Scanning... Station is 1510 AM
Switching to FM
Scanning... Station is 89.1 FM
Scanning... Station is 103.9 FM
Scanning... Station is 81.3 FM
Scanning... Station is 89.1 FM
Switching to AM
Scanning... Station is 1250 AM
Scanning... Station is 1380 AM
"""


def main():
    radio = Radio()
    actions = [radio.scan] * 2 + [radio.toggle_amfm] + [radio.scan] * 2
    actions *= 2

    with redirect_stdout(io.StringIO()) as output:
        for action in actions:
            action()
    assert output.getvalue() == CORRECT_OUTPUT


if __name__ == "__main__":
    main()
