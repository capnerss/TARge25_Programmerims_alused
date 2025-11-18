"""Math exercises vol2."""
import math

def time_converter(seconds: int) -> str:
    """Convert time in seconds to hours and minutes."""
    hours, remind = divmod(seconds, 3600)
    minutes, remind = divmod(remind, 60)
    return f"{seconds} sekundit on {hours} tund(i) ja {minutes} minut(it)."


def student_helper(angle: int) -> str:
    """Return the sine and cosine of the given angle in degrees."""
    # Write your code here
    sine = round(math.sin(math.radians(angle)), 1)
    cosine = round(math.cos(math.radians(angle)), 1)
    return f"Nurk: {angle}, siinus: {sine}, koosinus: {cosine}."


def greetings(n: int) -> str:
    """Return a string that contains "Hey" n times."""
    # Write your code here
    lots_of_heys = "Hey" * n
    return lots_of_heys


def adding_numbers(num_a: int, num_b: int) -> str:
    """Return given numbers added together as a string."""
    # Write your code here
    string_numbers = str(num_a) + str(num_b)
    return string_numbers


if __name__ == '__main__':
    time_convert = time_converter(3660)
    assert time_convert == "3660 sekundit on 1 tund(i) ja 1 minut(it)."

    helper = student_helper(45)
    assert helper == "Nurk: 45, siinus: 0.7, koosinus: 0.7."

    greet = greetings(3)
    assert greet == "HeyHeyHey"

    adding = adding_numbers(5,5)
    assert adding == "55"
