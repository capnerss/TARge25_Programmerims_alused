"""Zoo."""
from zoo import Zoo
from animal import Animal


leo = Animal("Leo", "lõvi", 5)
mia = Animal("Mia", "ahv", 2)
teine_leo = Animal("Leo", "lõvi", 3)
karl = Animal("Karl", "karu", 8)

tallinna_loomaaed = Zoo("Tallinna Loomaaed", 3)

tallinna_loomaaed.add_animal(leo)
tallinna_loomaaed.add_animal(mia)

tallinna_loomaaed.add_animal(teine_leo)

tallinna_loomaaed.add_animal(karl)

print("Kõik loomad:", tallinna_loomaaed.get_all_animals())
print("Vanuse järgi:", tallinna_loomaaed.get_animals_by_age())
print("Tähestiku järgi:", tallinna_loomaaed.get_animals_sorted_alphabetically())