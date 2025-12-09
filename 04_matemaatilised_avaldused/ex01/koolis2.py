"""Ülesanne 1
Koosta programm, mis küsib kasutajalt ristküliku lähiskülgede pikkused ning väljastab ekraanile ristküliku ümbermõõdu ja pindala."""


def compute_triangle():
    lenght = float(input("Siseta pikkus"))
    height = float(input("Siseta laius"))
    area = lenght * height
    dala = 2 * (lenght * height)
    print(f"Pindala on {area}")
    print(f"Umbermoot on {dala}")


"""Ülesanne 2
Koosta programm, mis küsib kasutajalt nime ja vanust ja väljastab ekraanile nimelise tervituse koos tekstiga, 
mis ütleb, kas tegemist on 7-18-aastase inimesega."""


def age_validation(age):
    if 7 <= age <= 18:
        return f"oled 7-18 aastane"
    else:
        return f"oled kas liga vana voi liga noor"


def name_greet(name):
    return f"Hello {name}"

"""Ülesanne 3
Koosta lihtne kalkulaator. Kasutajalt küsitakse kaks arvu ja tehtemärk ning seejärel kuvatakse tehe koos vastusega. Näiteks:

Sisestage esimene arv: 2
Sisestage teine arv: 3
Sisestage tehe: +
Tulemus: 2+3=5"""


def dog_calculator(number_1:float, number_2:float, operation:str)->str:
    result = 0
    if operation == "+":
        result = number_1 + number_2
    elif operation == "-":
        result = number_1 - number_2
    elif operation == "/":
        result = number_1 / number_2
    elif operation == "*":
        result = number_1 * number_2
    elif operation == "**":
        result = number_1 ** number_2
    elif operation == "//":
        result = number_1 // number_2
    elif operation == "%":
        result = number_1 % number_2
    else:
        return f"Urrrr"
    return f"{result * "auh "}"


if __name__ == "__main__":
    # # compute_triangle()
    # name = input("Mis on sinu nimi?")
    # age = int(input("Mis on sinu vanus?"))
    # print(f"{name_greet(name)}, {age_validation(age)}")
    number_1 = int(input())
    number_2 = int(input())
    tehe = input()
    print(calculator(number_1, number_2, tehe))