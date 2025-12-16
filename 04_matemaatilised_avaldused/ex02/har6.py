"""
Ülesanne 6
Loo programm, mis küsib kasutajalt ruutvõrrandi liikmete (ruutliige, lineaarliige, vabaliige)
kordajad ning arvutab nende põhjal diskriminandi ja väljastab selle põhjal ruutvõrrandi lahendid.
Nagu tead, võib lahendeid vastavalt diskriminandi väärtusele olla üks või kaks, kuid lahendid võivad ka puududa.
"""
import math


def calculate_discriminatal(a: float, b: float,c: float)->float:
    return b ** 2 - 4 * a * c


def solve_quadratic_equsion(a, b, discriminant, useAddition):
    if useAddition:
        top = -b + math.sqrt(discriminant)
    else:
        top = -b - math.sqrt(discriminant)
    bottom = 2 * a
    return top / bottom


if __name__ == "__main__":
    print("Arvutame ruutvorrandit")
    a = float(input("Sissesta ruutliige"))
    if a == 0:
        print("Ruutliige ei tohi olla null")
    else:
        b = float(input("Sisseta lineaarliige"))
        c = float(input("Sisseta vabalige"))
        discriminant = calculate_discriminatal(a,b,c)
        if discriminant < 0:
            print("Lahendid puuduvad")
        elif discriminant == 0:
            solution = solve_quadratic_equsion(a,b,discriminant, True)
            print(f"Lahendid on vordsed: {solution}")
        else:
            solution = solve_quadratic_equsion(a, b, discriminant, True)
            solution2 = solve_quadratic_equsion(a, b, discriminant, False)
            print(f"Lahendid on kaks: {solution} ja {solution2}")