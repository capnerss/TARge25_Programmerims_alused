"""Ülesanne 7
Eestis kasutatav isikukood koosneb üheteistkümnest numbrist.
Tutvu isikukoodi struktuuriga (https://et.wikipedia.org/wiki/Isikukood) ja kirjuta programm,
 mis analüüsib isikukoode ja väljastab võimalikult rohkem infot selle kohta (sünnikuupäev, sugu jne).
  Isikukoodi käsitlege kui sümbolite kogumit ehk sõnet (kuigi see koosneb numbritest), analüüsimiseks kasutage sõneoperatsioone (vt. käsiraamat).
   Kuna isikukoode on keeruline testimise ajal korduvalt sisestada, on alguses mõistlik sisestada erinevad isikukoodid
   ning kommenteerida vastavalt vajadusele ülearused välja, näiteks järgnevalt kasutatakse teisel real olevat isikukoodi:

#isikukood = "60201302715"
isikukood = "48008082727"
#isikukood = "31212230156"
[...]
Hiljem võib lisada isikukoodi küsimise kasutajalt.

Täiendusi:

Vastavalt toodud isikukoodi tutvustavale artiklile võrdle esimest kümmet numbrit
 ja viimast numbrit (nn. kontrollnumbrit), et teha selgeks, kas isikukood on üldse kehtiv.
  Kuna isikukoodi võtame kui sõnet, aga seal olevaid arve on vaja korrutada, peame tegema tüübiteisenduse:
   sõnena oleva arvu peame teisendama täisarvuks (funktsioon "int()").
Koosta funktsioon, mis ise automaatselt koostab kehtivaid isikukoode. Võimatud on näiteks isikukoodid vale kontrollnumbriga,
 kuid ka sellised, mis viitavad olematule kuupäevale (algusega "3950230...", mis tähendaks 30. veebruari) vms.
  Vali kas "ohutu" tee (ette on antud piirid, mis kehtivad igal juhul) või loo sisemised sõltuvused
   (stiilis "kui kuu on aprill, siis maksimaalsete päevade arv on 30")."""
from datetime import date


def has_correct_cheksum(id_code):
    return get_checksum(id_code) == int(id_code[-1])


def is_valid(id_code):
    return len(id_code) == 11 and id_code.isdigit() and has_correct_cheksum(id_code)


def get_century(id_code):
    centurys_id = {"1" : "18", "2" : "18", "3" : "19", "4" : "19", "5" : "20", "6" : "20", "7" : "2100", "8" : "2100"}
    return centurys_id.get(id_code[0])


def get_gender(id_code):
    gender_id = { "2" : "18", "4" : "19", "6" : "20", "8" : "2100"}
    if id_code in gender_id.keys():
        gender = "naine"
    else:
        gender = "mees"
    return gender



def get_year(id_code, century):
    return get_century(id_code) + id_code[1:3]


def get_month(id_code):
    return id_code[3:5]


def get_day(id_code):
    return id_code[5:7]


def get_birth_date(year, month, day):
    return f"{year}, {month}, {day}"


def decode_id_code(id_code: str):
    if is_valid(id_code):
        century = get_century(id_code)
        gender = get_gender(id_code)
        year = get_year(id_code, century)
        month = get_month(id_code)
        day = get_day(id_code)
        birth_date = get_birth_date(year, month, day)
        print(gender, birth_date)
    else:
        print("Vigane id")


def get_product_sum(id_code, list1):
    return_sum = 0
    for index, weight in enumerate(list1):
        id_number = int(id_code[index])
        product = id_number *weight
        return_sum +=product
    return return_sum


def get_checksum(id_code: str)-> int:
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    list2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    product_sum = get_product_sum(id_code, list1)
    remainder = product_sum % 11
    if remainder < 10:
        return remainder
    product_sum = get_product_sum(id_code, list2)
    remainder = product_sum % 11
    if remainder < 10:
        return remainder
    return 0


if __name__ == '__main__':
    #isikukood = "60201302715"
    isikukood = "48008082727"
    # isikukood = "31212230156"
    decode_id_code(isikukood)
