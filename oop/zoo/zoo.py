from animal import Animal


class Zoo:
    def __init__(self, name: str, max_number_of_animals: int):
        self.name = name
        self.max_number_of_animals = max_number_of_animals
        self.animals = []

    def can_add_animal(self, animal: Animal) -> bool:
        if len(self.animals) >= self.max_number_of_animals:
            return False
        if animal in self.animals:
            return False
        for existing_animal in self.animals:
            if existing_animal.name == animal.name and existing_animal.specie == animal.specie:
                return False
        return True

    def add_animal(self, animal: Animal):
        if self.can_add_animal(animal):
            self.animals.append(animal)

    def can_remove_animal(self, animal: Animal) -> bool:
        return animal in self.animals

    def remove_animal(self, animal: Animal):
        if self.can_remove_animal(animal):
            self.animals.remove(animal)

    def get_all_animals(self) -> list:
        return self.animals

    def get_animals_by_age(self) -> list:
        return sorted(self.animals, key=lambda animal: animal.age)

    def get_animals_sorted_alphabetically(self) -> list:
        return sorted(self.animals, key=lambda animal: animal.name)