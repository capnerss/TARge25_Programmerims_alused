"""Bänner"""
from numpy.core.defchararray import upper


def banner(reklaamlause: str):
    """Tagastab reklaamlause, kus kõik tähed on suured tähed."""
    return upper(reklaamlause)


korda_kuvada = int(input("Mitu korda soovitakse reklaamlauset kuvada?"))
input_reklaamlause = banner(input("Millist reklaamlauset soovib kasutada?"))
for i in range(korda_kuvada):
    print(input_reklaamlause)