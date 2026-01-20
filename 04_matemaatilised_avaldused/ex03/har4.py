"""Ülesanne 4
Koosta mäng, kus saate ära arvata arvuti poolt mõeldud täisarvu ühest kahekümneni. nt:

Mõtlesin ühele täisarvule 1-20ni. Mis arv see on?
>> 15
Liiga suur, proovi uuesti.
>> 7
Liiga väike, proovi uuesti.
>> 9
Liiga väike, proovi uuesti.
>> 11
Tubli, arvasid ära. Arv oli 11.
Enne ülesande lahendamist mõelge välja mängu algoritm ja koostage selle kohta plokkskeem."""


from random import randint


def arva_arv():
    arv = randint(1,21)
    for i in range(5):
        user_input = int(input("Mõtlesin ühele täisarvule 1-20ni. Mis arv see on?"))
        if user_input == arv:
            print(f"Tubli, arvasid ära. Arv oli {arv}.")
            break
        elif user_input > arv:
            print("Liiga suur, proovi uuesti.")
        else:
            print("Liiga väike, proovi uuesti")
    print(f"Arv oli {arv}.")


if __name__=="__main__":
    arva_arv()
