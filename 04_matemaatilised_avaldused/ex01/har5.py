"""Elektrihind."""


def elektrihind(kilovatt_tunni: float)->float:
    """Tagastab hinna eurodes megavatt-tunni kohta."""
    megavatt_tunni = kilovatt_tunni * 10
    return megavatt_tunni


input_killovat = input("Sisesta elektrihind sentides kilovatt-tunni kohta:")
output_megavatt = elektrihind(float(input_killovat))
print(f"{input_killovat} s/kWh on {output_megavatt} €/MWh")
