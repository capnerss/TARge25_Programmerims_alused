"""
Ülesanne 4
Koosta programm, mis küsib kasutajalt rea, mille järele ta soovib failis luuletus.txt uut rida lisada ning seejärel lisab kasutaja poolt sisestatud rea nt:

Sisesta rida, mille järele soovid uut rida lisada:
>> Padja, teki viskan maha,
Sisesta rida, mida soovid lisada:
>> üles ärgata ma ei taha,
Tulemus failis luuletus.txt:

Hommikul kui üles ärkan,
arvutit ma laual märkan.
Padja, teki viskan maha,
üles ärgata ma ei taha,
jooksen ruttu compu taha.
Kiirelt sisestan parooli,
kuid juba tuleb minna kooli.
Error tuleb ette siis,
kool on mulle räme piin.
"""
import exc_02 as maker

def search_line(filen, poeml, nline):
    poem = []
    with open(filen, "r", encoding="utf-8") as f:
        for index, i in enumerate(f):
            if list(i)[:(len(i)-1)] == list(poeml):
                poem.append(nline+"\n")
            poem.append(i)
        print(poem)
    return poem





if __name__ == '__main__':
    maker.text_to_file(maker.text_for_file)
    new_line = input("Enter new line: ")
    poem_line = input("Enter line: ")
    maker.text_to_file(search_line("luuletus.txt", poem_line, new_line))