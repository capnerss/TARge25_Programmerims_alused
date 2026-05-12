"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""

    pass


class Person:
    """Represent person with firstname, lastname and age."""

    def __init__(self):
        self.firstname = ""
        self.lastname = ""
        self.age = ""


class Student:
    """Represent student with firstname, lastname and age."""

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


if __name__ == '__main__':
    # empty usage
    e = Empty()
    # 3 x person usage
    p1 = Person()
    p1.firstname="Jon"
    # 3 x student usage
    s1 = Student(firstname="John", lastname="Doe", age=40)
    s2 = Student(firstname="Jon", lastname="Doe", age=50)
    s3 = Student(firstname="Jon", lastname="De", age=60)