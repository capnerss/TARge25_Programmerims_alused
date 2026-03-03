"""
Ülesanne 2
Tee uus fail luuletus.txt ning lisa sinna järgmine luuletus:

Hommikul kui üles ärkan,
arvutit ma laual märkan.
Padja, teki viskan maha,
jooksen ruttu compu taha.
Kiirelt sisestan parooli,
kuid juba tuleb minna kooli.
Error tuleb ette siis,
kool on mulle räme piin.
Koosta programm, mis kuvab ekraanile luuletuse read, kuid lisab nende ette rea järjekorranumbri ja iga rea järele sulgudesse reas asuvate sümbolite arvu e. rea pikkuse.
"""
text_for_file = ["Hommikul kui üles ärkan,",
"arvutit ma laual märkan.",
"Padja, teki viskan maha,",
"jooksen ruttu compu taha.",
"Kiirelt sisestan parooli,",
"kuid juba tuleb minna kooli.",
"Error tuleb ette siis,",
"kool on mulle räme piin."]

def text_to_file(textf):
    with open("luuletus.txt", "w", encoding="utf-8") as f:
        for line in textf:
            f.write(line +"\n")


def read_text(file_name):
    result = []
    with open(file_name, encoding="utf-8") as f:
        count = 1
        for line in f:
            result.append(f"{str(count)} {line.strip()}  {str(len(line)-1)}")
            print(f"{str(count)} {line.strip()}  {str(len(line)-1)}")
            count +=1
    return result

if __name__ == '__main__':
    text_to_file(text_for_file)
    read_text("luuletus.txt")