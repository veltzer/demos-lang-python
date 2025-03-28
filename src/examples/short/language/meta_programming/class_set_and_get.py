""" class_set_and_get.py """


class ValidString:
    def __init__(self, minlen=0, maxlen=None):
        self.minlen = minlen
        self.maxlen = maxlen
        self.name = None

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, None)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f"{self.name} must be a string")
        if len(value) < self.minlen:
            raise ValueError(f"{self.name} must be at least {self.minlen} characters long")
        if self.maxlen is not None and len(value) > self.maxlen:
            raise ValueError(f"{self.name} must be at most {self.maxlen} characters long")
        instance.__dict__[self.name] = value


class Person:
    name = ValidString(minlen=2, maxlen=30)
    email = ValidString(minlen=5, maxlen=100)

    def __init__(self, name, email):
        self.name = name
        self.email = email


if __name__ == "__main__":
    # Valid usage
    person = Person("John Doe", "john.doe@example.com")
    print(f"Name: {person.name}, Email: {person.email}")

    # Invalid usage examples
    try:
        Person("J", "john.doe@example.com")  # Name too short
    except ValueError as e:
        print(f"Error: {e}")

    try:
        Person("John Doe", "john")  # Email too short
    except ValueError as e:
        print(f"Error: {e}")

    try:
        Person("John Doe", 12345)  # Email is not a string
    except ValueError as e:
        print(f"Error: {e}")

    # Modifying attributes
    person.name = "Jane Doe"
    print(f"Updated name: {person.name}")

    try:
        person.email = "invalid"  # Too short
    except ValueError as e:
        print(f"Error: {e}")
