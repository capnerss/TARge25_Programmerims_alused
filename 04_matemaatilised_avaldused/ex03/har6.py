"""Ülesanne 6
Väljasta ekraanile kõikvõimalikud kombinatsioonid kujul "x - y - z", kus x, y ja z on mistahes täisarvud 1-st 20-ni (20 kaasaarvatud). Samuti loenda, mitu sellist kombinatsiooni leiti. Tulemus:

1 - 1 - 1
1 - 1 - 2
​1 - 1 - 3
[...]
​15 - 12 - 2
​15 - 12 - 3
[...]
20 - 20 - 19
20 - 20 - 20
Kokku leiti 8000 kombinatsiooni."""

count = 0
for x in range(20):
    for y in range(20):
        for z in range(20):
            print(f"{x + 1} - {y + 1} - {z + 1}")
            count+=1
print(count)