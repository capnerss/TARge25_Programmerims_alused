"""
Phonebook

1.Peab saama sisestada nime ja telefoni numbrit.
2.Samal nimel võib olla ainult üks telefoni number.
3.Peab saama küsida nime järgi numbrit ja numbri järgi nime.
    a.Kui vastet pole, siis peab võimaldama lisamist.
4.Programmi sulgemine ei tohi andmeid kaotada (tuleb salvestada faili).
5.Lisa funktsioon terve raamatu kuvamiseks.
"""
import csv


phone_book_dict = {}


def lae_andmed():
    """Loeb andmed failist, kui fail on olemas."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def salvesta_andmed(andmed):
    """Salvestab andmed faili."""
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        json.dump(andmed, f, ensure_ascii=False, indent=4)


def lisa_kontakt(andmed, nimi=None, number=None):
    """Lisab uue kontakti või uuendab olemasolevat."""
    if not nimi:
        nimi = input("Sisesta nimi: ").strip()
    if not number:
        number = input("Sisesta telefoni number: ").strip()

    andmed[nimi] = number
    salvesta_andmed(andmed)
    print(f"--> Salvestatud: {nimi} - {number}")


def otsi_nime_jargi(andmed):
    """Otsib numbrit nime alusel."""
    nimi = input("Sisesta otsitav nimi: ").strip()
    if nimi in andmed:
        print(f"--> {nimi} telefoninumber on {andmed[nimi]}")
    else:
        print("--> Vastet ei leitud.")
        lisa = input("Kas soovid selle nime uue numbriga lisada? (j/e): ").strip().lower()
        if lisa == 'j':
            lisa_kontakt(andmed, nimi=nimi)


def otsi_numbri_jargi(andmed):
    """Otsib nime numbri alusel."""
    number = input("Sisesta otsitav number: ").strip()
    leitud = False

    for nimi, tel_nr in andmed.items():
        if tel_nr == number:
            print(f"--> Number {number} kuulub isikule: {nimi}")
            leitud = True
            break

    if not leitud:
        print("--> Vastet ei leitud.")
        lisa = input("Kas soovid selle numbri uue nimega lisada? (j/e): ").strip().lower()
        if lisa == 'j':
            lisa_kontakt(andmed, number=number)


def kuva_koik(andmed):
    """Kuvab kogu telefoniraamatu sisu."""
    if not andmed:
        print("--> Telefoniraamat on tühi.")
        return

    print("\n--- Kogu telefoniraamat ---")
    for nimi, number in andmed.items():
        print(f"{nimi}: {number}")
    print("---------------------------")


def main():
    andmed = lae_andmed()

    while True:
        print("\n--- MENÜÜ ---")
        print("1. Lisa uus kontakt")
        print("2. Otsi numbrit nime järgi")
        print("3. Otsi nime numbri järgi")
        print("4. Kuva kogu telefoniraamat")
        print("5. Välju")

        valik = input("Tee valik (1-5): ").strip()

        if valik == '1':
            lisa_kontakt(andmed)
        elif valik == '2':
            otsi_nime_jargi(andmed)
        elif valik == '3':
            otsi_numbri_jargi(andmed)
        elif valik == '4':
            kuva_koik(andmed)
        elif valik == '5':
            print("Programm suletakse. Andmed on turvaliselt salvestatud!")
            break
        else:
            print("--> Vigane valik, proovi uuesti.")


if __name__ == "__main__":
    main()