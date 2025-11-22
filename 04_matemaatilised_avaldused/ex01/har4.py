"""Function examples."""


def func():
    """Prindi konsooli I´m inside the function."""
    print("I´m inside the function")


def my_name_is(name: str):
    """Prindi konsooli My name is [name], kus [name] asemel prinditakse functiooni sisendiks antud nimi."""
    print(f"My name is {name}")


def sum_six(num: int):
    """Tagasta(return) number 6 ja funktiooni sisendi summa."""
    return num + 6


def sum_numbers(a: int, b: int):
    """Tagasta(return) sisendite summa."""
    return a + b


def usd_to_eur(usd: int):
    """Tagasta funktsioon summa eurodes."""
    return usd * 0.8