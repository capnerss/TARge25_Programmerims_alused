"""
Ülesanne 3
Lihtsa sõnaraamatu jaoks koosta neli järjendit (arv, eesti, inglise, itaalia) sisuga:
 arv - 1, 2, 3, 4
 eesti - üks, kaks, kolm, neli
 inglise - one, two, three, four
 itaalia - uno, due, tre, quattro

Väljasta kõik elemendid tabelina ekraanile: 1 - üks - one - uno 2 - kaks - two - due ...

Lisa arvude ja eesti järjendile veel kaks elementi.
Kontrolli, kas itaalia sõnade järjendis eksiteerib element 'tre'
Väljasta kõigi nelja järjendi elemendid tähestikulises järjekorras kasvavalt.
"""


arv = [1, 2, 3, 4]
eesti = ["üks", "kaks", "kolm", "neli"]
inglise = ["one", "two", "three", "four"]
itaalia = ["uno", "due", "tre", "quattro"]

for i in range(len(arv)):
    print(f"{arv[i]} - {eesti[i]:^4} - {inglise[i]:^5} - {itaalia[i]:^7}")
if "tre" in itaalia:
    print("'tre' eksisterib itaalia jarjendis")