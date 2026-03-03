"""
Ülesanne 3
Tee programm, mis väljastab failist luuletus.txt kasutaja poolt soovitud rea nt:

Mitmendat rida soovid kuvada:
>> 7
Error tuleb ette siis,
NB! Faili avamiseks ja rea väljastamiseks koosta eraldi alamprogramm (ehk funktsioon).
"""


def read_fail_line(failn, row_number):
    index = 1
    with open(failn, "r", encoding="utf-8") as f:
        for i in f:
            if index == row_number:
                print(i)
            index += 1


def wait_for_input():
    result = input("Mitmendat rida soovid kuvada: ")
    return int(result)


if __name__ == '__main__':
    read_fail_line("luuletus.txt", wait_for_input())