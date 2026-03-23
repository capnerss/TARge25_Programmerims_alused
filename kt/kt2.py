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


def phone_book():
    """search number in phone_book_dict.txt by name or number, or add it."""
    phone_book_dict = {}
    try:
        with open("phone_book.txt", "r") as book:
            csvreader = csv.reader(book, delimiter=" ")
            for row in csvreader:
                phone_book_dict[row[0]] = row[1]
            book.close()
    except FileNotFoundError:
        with open("phone_book.txt", "w") as book:
            book.close()
    while True:
        answer = input("Exit? 'E' or Show PhoneBook? 'B' or Search by phone number 'P' or by Name 'N' or Add 'A': ")
        if answer.upper() == "N":
            omanik = input("Siseta numbri omaniku nime: ")
            if omanik in phone_book_dict:
                print(f"{omanik} - {phone_book_dict[omanik]}")
        else:
            number = input("Pole numbrid. Siseta numbri: ")
            phone_book_dict[omanik] = number
            print(f"{omanik} - {phone_book_dict[omanik]}")
        if answer.upper() == "E":
            with open("phone_book.txt", "w") as book:
                for keys, values in phone_book_dict.items():
                    book.write(keys +" " + values + "\n")
            break
        if answer.upper() == "B":
            for keys, values in phone_book_dict.items():
                print("nimi: " + keys + " " + "tel: " + values )
            break

if __name__ == '__main__':
    phone_book()
