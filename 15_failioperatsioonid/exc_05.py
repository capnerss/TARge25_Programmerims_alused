"""
Ülesanne 5
Palindroomiks nimetatakse sõna (ka sõnaühendit), mis on nii vasakult paremale kui paremalt vasakule lugedes täpselt ühesugunem (näit. "kook", "kuulilennuteetunneliluuk" jne).
 Loo programm, mis trükib ekraanile välja kõik tekstifailis olevad sõnad, mis on palindroomid.
Alustekstiks võid kasutada suvalist teksti, kuid katsetada tasuks ka sõnaloenditega, kus iga sõna asub eraldi real (näit. eesti keele sõnade algvormid e. lemmad veebilehelt http://www.eki.ee/tarkvara/wordlist/).
"""
import exc_02 as maker

def tenet(filen):
    result = []
    with open(filen, "r", encoding="utf-8") as f:
        for i in f:
            bag = i.strip()
            if bag == bag[::-1]:
                result.append(bag)
    return result


if __name__ == '__main__':
    maker.text_to_file(maker.text_for_file)
    print(tenet("tuttavad1.txt"))