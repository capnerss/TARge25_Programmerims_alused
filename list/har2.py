"""
Koosta järjend vähemalt kümne Euroopa pealinnaga (suvalises järjekorras).

Väljasta linnad eraldi ridadena.
Järjesta need tähestikulisse järjekorda.
Lase kasutajal lisada kaks uut Euroopa pealinna ja järjesta uuesti.
Esita linnade nimed tähestikulises järjekorras, lisades iga nime ette ka järjekorra numbri.
Lisa väljundile kokkuvõttev lause "Meie järjendis on 12 Euroopa pealinna", kus linnade arv leitakse vastava funktsiooni abil.
"""


capitals =["Tallinn", "Riga", "Vilnius", "Helsinki", "Roma", "Oslo", "Valga", "Sooru", "Soo", "Pikk"]


def print_list(elements: list):
    for i in elements:
        print(i)


def sort_list(element: list):
    element.sort()

def add_capitals(capitalos, amount):
    for i in range(amount):
        capitalos.append(input(f"{i + 1}. Siseta capitals"))


def print_list_numbers(capitalos):
    for index, element in enumerate(capitalos):
        print(f"{index + 1}. {element}")

def summarize(capitalos):
    print(f"Meie järjendis on {len(capitalos)} Euroopa pealinna")


if __name__ == '__main__':
    add_capitals(capitals, 2)
    sort_list(capitals)
    print(capitals)
    print_list_numbers(capitals)
    summarize(capitals)
