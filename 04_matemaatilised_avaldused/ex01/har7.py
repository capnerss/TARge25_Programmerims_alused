"""Peo eelarve."""


def eelarve(kulaliste_arv: int)->int:
    """Tagastab eelarve kogusumma. Näiteks argumendiga 5 tagastab funktsioon arvu 105."""
    return 55 + kulaliste_arv * 10


input_kulaliste_kutse_arv = int(input("Mitu inimest on peole kutsutud?"))
input_kulaliste_tegelik_arv = int(input("Mitu inimest tuleb?"))
print(f"Maksimaalne eelarve on {eelarve(input_kulaliste_kutse_arv)} eurot")
print(f"Minimaalne eelarve on {eelarve(input_kulaliste_tegelik_arv)} eurot")