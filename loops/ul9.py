"""
Koosta programm, mis "viskab täringut" kolm korda ehk väljastab ekraanile 3 juhusliku täringuviske tulemused.
Et ekraanipilt oleks realistlikum, esita tulemused graafiliselt, selleks kasuta nn. ASCII graafikat (https://en.wikipedia.org/wiki/ASCII_art): imiteeri tekstisümbolite abil täringu külje kujutist.
Täiendamiseks:
Kasutaja võib alguses ise valida, mitu korda täringut visata.
Mängida võib mitu inimest, programmi alguses küsitakse inimeste nimesid.
Täringut imiteeritakse kolmemõõtmelisena.
"""
from random import randint


def random_number_generator(rolls):
    numbers = []
    for i in range(rolls):
        numbers.append(numbers_to_graphic(randint(1, 6)))
    return numbers


def roll_a_dice():
    players_list = []
    players = int(input("Kui palju mängijad?: "))
    for i in range(players):
        players_list.append(input("Sista mangija nimi!: "))
    rolls = int(input("Kui palju korda viskad?: "))
    player_rolls(players_list, rolls)


def player_rolls(players_list, rolls):
    for i in players_list:
        print(f"{i} viskas numbrid {random_number_generator(rolls)}")


def numbers_to_graphic(num):
    pictures = { 1 : "*",
                 2 : "**",
                 3 : "***",
                 4 : "****",
                 5 : "*****",
                 6 : "******",}
    return pictures[num]

if __name__ == '__main__':
    roll_a_dice()
