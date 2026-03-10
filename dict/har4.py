"""
Ülesanne 4
Lisa kõikidesse sõnastikesse järgmised sõnad:

headaega - goodbye - arrivederci
pott - pot - pentola
sõnastik - dictionary - dizionario
Tõlgi (väljastage ekraanile) järgmised sõnad:

üks -> itaalia
ciao - > eesti
dog -> itaalia
pentola - inglise
"""
import har3 as dicts

dicts.italia_dict["uks"] = "uno"

def dicts_adder(eesti_string, english_string, itaalia_string):
    dicts.english_dict[eesti_string] = english_string
    dicts.italia_dict[eesti_string] = itaalia_string
    dicts.english_eesti_dict[english_string ]= eesti_string
    dicts.italia_eesti_dict[itaalia_string] = eesti_string


if __name__ == '__main__':
    dicts_adder("headaega", "goodbye", "arrivederci")
    dicts_adder("pott", "pot", "pentola")
    dicts_adder("sõnastik", "dictionary", "dizionario")
    print(dicts.english_dict)
    print(dicts.italia_dict)
    print(dicts.italia_dict["uks"])
    print(dicts.italia_eesti_dict["ciao"])
    print(dicts.italia_dict[dicts.english_eesti_dict["dog"]])
    print(dicts.english_dict[dicts.italia_eesti_dict['pentola']])



