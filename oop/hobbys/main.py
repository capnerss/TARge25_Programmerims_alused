"""Hobbies but OOP."""
from person import *



if __name__ == '__main__':
    person1 = Person("Mari", "Kukk", ["dancing", "biking", "programming"])
    person2 = Person("Jeff", "Bezos", ["money", "hair", "late_capitalism", "space", "unions"])
    person3 = Person("Elon", "Musk", ["late_capitalism", "space", "cars"])
    people = [person1, person2, person3]
    print(sort_by_most_hobbies(people))  # -> [JeffBezos, ElonMusk, MariKukk]
    print(sort_by_least_hobbies(people))   # -> [ElonMusk, MariKukk, JeffBezos]
    print(filter_by_hobby(people, "space"))  # Oodatav filtri tulemus (järjekord algse listi põhjal)
    print(sort_people_and_hobbies(people))  # -> [ElonMusk, JeffBezos, MariKukk]
    print(person1.hobbies)  # -> ['biking', 'dancing', 'programming']