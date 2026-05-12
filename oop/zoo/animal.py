class Animal:
    def __init__(self, name: str, specie: str, age: int):
        self.name = name
        self.specie = specie
        self.age = age
    def __repr__(self):
        return f"{self.name} ({self.specie}, {self.age} aastat)"


