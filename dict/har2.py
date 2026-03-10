"""
Ülesanne 2
Tõlgi (väljasta ekraanile) järgmised sõnad:

tere -> inglise k, itaalia k
auto -> itaalia k
kass - > inglise k
üks -> itaalia k
kolm -> inglise k
"""
from har1 import english_dict, italia_dict

italia_dict["uks"] = "uno"
english_dict["kolm"] = "three"

if __name__ == "__main__":
    print(english_dict["tere"], italia_dict["tere"])
    print(italia_dict["auto"])
    print(english_dict["kass"])
    print(italia_dict["uks"])
    print(english_dict["kolm"])
