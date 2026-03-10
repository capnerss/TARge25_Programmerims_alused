"""Cooper testis mõõdetakse, kui palju suudab inimene joosta 12 minutiga.
 On määratud erinevad hindenormid meestele ja naistele."""
import csv


def hinda(distance:int, sex:str):
    if sex == 'M':
        if distance >= 2800:
            print(f"{sex} {distance} m, väga hea")
        elif distance >= 2000:
            print(f"{sex} {distance} m, rahuldav, järgmisest hindest puudu {2800-distance} m")
        else:
            print(f"{sex} {distance} m, nõrk, järgmisest hindest puudu {2000-distance} m")
    elif sex =='N':
        if distance >= 2600:
            print(f"{sex} {distance} m, väga hea")
        elif distance >= 1800:
            print(f"{sex} {distance} m, rahuldav, järgmisest hindest puudu {2600-distance} m")
        else:
            print(f"{sex} {distance} m, nõrk,järgmisest hindest puudu {1800-distance} m")


if __name__ == '__main__':
    input_date = input("Sisestage failinimi:  ")
    with open(input_date, "r") as f:
        csvreader = csv.reader(f, delimiter=" ")
        for row in csvreader:
            hinda(int(row[0]), row[1])