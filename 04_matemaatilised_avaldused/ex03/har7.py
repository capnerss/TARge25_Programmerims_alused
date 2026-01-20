"""Ülesanne 7
Koosta programm, mis küsib kasutajalt arvu N ja väljastab O-tähtedest koosneva ruudu suuruses NxN. Seejärel muutke programmi nii, et ruudu diagonaalidel olevad märgid oleksid X-d, näiteks:

X O O O O O O O X
O X O O O O O X O
O O X O O O X O O
O O O X O X O O O
O O O O X O O O O
O O O X O X O O O
O O X O O O X O O
O X O O O O O X O
X O O O O O O O X
... või (paarisarvulise N-i puhul):

X O O O O O O O O X
O X O O O O O O X O
O O X O O O O X O O
O O O X O O X O O O
O O O O X X O O O O
O O O O X X O O O O
O O O X O O X O O O
O O X O O O O X O O
O X O O O O O O X O
X O O O O O O O O X
Tühikuid võid lisada vastavalt oma soovile."""


def print_sqr(size):
    for row in range(size):
        for col in range(size):
            if row == col or row+col==size-1:
                print("X", end=" ")
            else:
                print("O", end =" ")
        print()


if __name__ == '__main__':
    size = int(input("Siste arv"))
    print_sqr(size)