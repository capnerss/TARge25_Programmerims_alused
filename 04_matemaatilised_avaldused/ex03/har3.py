"""Ülesanne 3
Koosta programm, mis aitab lastel treenida liitmist. Programm peaks pakkuma välja juhuslike arvudega liitmistehteid ning ootama kasutajalt vastust. Kui vastus on õige, kiitma kasutajat, kui aga vale, andma õige vastuse ja esitama uue tehte. Järjest esitatavate tehete hulk võib olla programmis ette antud (näiteks 10), samuti võib olla ette antud piirid, kui suuri arve kasutajalt küsitakse (näiteks 1 kuni 50). Programm peaks pidama arvestust ka õigete vastuste üle ning väljastama pärast viimast tehet tulemuse. Näiteks:

Tere! Õpime arvutama. Esitan 10 liitmistehet, püüa vastata õigesti.
5 + 16 =
>> 21
Tubli, õige vastus!
18 + 23 =
>> 39
Sinu vastus polnud õige. Õige vastus on 41.
[...]
2 + 5 =
>> 7
Tubli, õige vastus!
See oli viimane ülesanne. Kogusid 10-st punktist 7.
Täiendusi vabal valikul:

Programm lubab kasutajal alguses sisestada, mitut tehet soovitakse.
Esitatavate arvude piirid saab kasutaja ette anda (maksimum või nii miinimum kui maksimum).
Küsitakse mitte ainult liitmistehteid, vaid ka teisi (lahutamine, korrutamine, jagamine).
Vastavalt lõpptulemusele reageeritakse erinevalt: "Ülihea!", "Olid tubli!", "Korralik keskmine tulemus!", "Püüad järgmisel korral rohkem." vms."""



from random import randint, choice
import operator




def treenida_liitmist(min_num:int, max_num:int, count:int):
    points = 0
    for i in range(count):
        rand_num1 = randint(min_num, max_num)
        rand_num2 = randint(min_num, max_num)
        operations = {"+":operator.add(rand_num1,rand_num2), "-":operator.sub(rand_num1,rand_num2) }
        result = choice(operations)
        print(f"Harjutus {i+1}/{count}-st")
        user_input = int(input(f"{rand_num1} + {rand_num2} = "))
        if  user_input == result:
            print("Tubli, õige vastus!")
            points+=1
        else:
            print(f"Sinu vastus polnud õige. Õige vastus on {result}.")
    print(f"See oli viimane ülesanne. Kogusid {count}-st punktist {points}.")

if __name__=="__main__":
    count = int(input("Kui palju harjutuse?"))
    min_num = int(input("Minimalne number"))
    max_max = int(input("Max number"))
    treenida_liitmist(min_num,max_num,count)