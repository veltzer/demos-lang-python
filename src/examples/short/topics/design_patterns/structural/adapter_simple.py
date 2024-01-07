"""
*What is this pattern about?
The Adapter pattern provides a different interface for a class. We can
think about it as a cable adapter that allows you to charge a phone
somewhere that has outlets in a different shape. Following this idea,
the Adapter pattern is useful to integrate classes that couldnt be
integrated due to their incompatible interfaces.

*What does this example do?

The example has classes that represent entities (Dog, Cat, Human, Car)
that make different noises. The Adapter class provides a different
interface to the original methods that make such noises. So the
original interfaces (e.g., bark and meow) are available under a
different name: make_noise.

*Where is the pattern used practically?
The Grok framework uses adapters to make objects work with a
particular API without modifying the objects themselves:
http://grok.zope.org/doc/current/grok_overview.html#adapters

*References:
http://ginstrom.com/scribbles/2008/11/06/generic-adapter-class-in-python/
https://sourcemaking.com/design_patterns/adapter
http://python-3-patterns-idioms-test.readthedocs.io/en/latest/ChangeInterface.html#adapter

*TL;DR
Allows the interface of an existing class to be used as another interface.
"""


class Toaster:
    def __init__(self) -> None:
        pass

    def toast(self, intesity) -> None:
        return "toasting!"
    def stop(self) -> None:
        return "stopped toasting!"

class ElectricAppliance:
    def __init__(self) -> None
        raise NotImplemented()
    def on(self) -> None
        raise NotImplemented()
    def off(self) -> None
        raise NotImplemented()

class ToasterToElectricApplianceAdapter:
    def __init__(self, toaster) -> None
        self.toaster = toaster
    def on(self) -> None
        toaster.toast(intensity=5)
    def off(self) -> None
        toaster.stop()
