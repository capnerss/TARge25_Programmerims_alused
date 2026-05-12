from main import *


def init_tests():
    P1 = Person("Mari", "Kukk", ["dancing", "biking", "programming"])
    P2 = Person("Jeff", "Bezos", ["money", "hair", "late_capitalism", "space", "unions"])
    P3 = Person("Elon", "Musk", ["late_capitalism", "space", "cars"])
    return [P1, P2, P3]

def test_sort_by_hobbies():
    people1 = init_tests()
    assert str(sort_by_most_hobbies(people1)) == "[JeffBezos, ElonMusk, MariKukk]"

def test_sort_by_least_hobbies():
    people1  = init_tests()
    assert sort_by_least_hobbies(people1) == ["ElonMusk", "MariKukk", "JeffBezos"]

def test_filter_by_hobbies():
    people1  = init_tests()
    assert filter_by_hobby(people1, "space") == ["JeffBezos", "ElonMusk"]

def test_sort_by_people_and_hobbies():
    people1  = init_tests()
    assert sort_people_and_hobbies(people1)  == ["ElonMusk", "JeffBezos", "MariKukk"]

def tests_person_hobbies():
    people1  = init_tests()
    assert person1.hobbies  == ['biking', 'dancing', 'programming']