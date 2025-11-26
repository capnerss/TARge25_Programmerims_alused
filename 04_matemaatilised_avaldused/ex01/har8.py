"""
Mündid
Euromüntide seerias on kuus erineva nimiväärtusega senti:
1 sent, 2 senti, 5 senti, 10 senti, 20 senti, 50 senti.
Sendid väärtustega 1, 2 ja 5 on pronksikarva (vasega kaetud teras),
sendid väärtustega 10, 20 ja 50 on kullakarva (vasesulam, mis sisaldab alumiiniumi, tsinki ja tina, nn Nordic Gold).
Peres on kombeks, et pronksikarva mündid panna hoiupõrsasse.
Müntide andmed on failis kirjas nii, et iga mündi väärtus on eraldi real."""


def pronksikarva_summa(mundid: list[int])->int:
    mundid= filter(lambda x: x == 1 or x == 2 or x == 5, mundid)
    return sum(mundid)


input_fail = input("Faili nime, milles asuvad sentide väärtused")
numbers = []
with open(input_fail, "r") as file:
    for line in file:
        numbers.append(int(line))
print(pronksikarva_summa(numbers))