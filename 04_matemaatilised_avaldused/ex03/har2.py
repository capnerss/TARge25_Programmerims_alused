"""
Ülesanne 2
Koosta programm, mis küsib kasutajalt 10 korda arve ja väljastab seejärel nende arvude summa.
 Täienda seda programmi nii, et kasutajalt küsitakse arve seni, kuni kasutaja enam uut arvu ei sisesta,
 vaid vajutab lihtsalt sisestusklahvi. Proovige seda ülesannet lahendada nii while- kui for-tsükliga.
"""


def solve_using_for():
    nubride_sum = 0
    for i in range(10):
        nubride_sum += float(input(f"Lisa arve {i+1}"))
    print(f"Sisetatud arvude summa on {nubride_sum}")


def solve_using_while():
    nubride_sum = 0
    i = 0
    while i < 10:
        nubride_sum += float(input(f"Lisa {i + 1} arve "))
        i+=1
    print(f"Sisetatud arvude summa on {nubride_sum}")


def solve_using_while_inf():
    nubride_sum = 0
    i = 0
    while True:
        numbrid = input(f"Lisa {i + 1} arve ")
        if numbrid.isdigit():
            break
        nubride_sum += int(numbrid)
        i += 1

    print(f"Sisetatud arvude summa on {nubride_sum}")


if __name__ == '__main__':
    #solve_using_for()
    #solve_using_while()
    solve_using_while_inf()
