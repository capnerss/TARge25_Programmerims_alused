"""Math exercises vol2."""
import math

def time_converter(seconds: int) -> str:
    """Convert time in seconds to hours and minutes."""
    hours, remainder = divmod(seconds, 3600)
    minutes, second = divmod(remainder, 60)
    return f"{seconds} sekundit on {hours} tund(i) ja {minutes} minut(it)."


def student_helper(angle: int) -> str:
    """Return the sine and cosine of the given angle in degrees."""
    sine = round(math.sin(math.radians(angle)), 1)
    cosine = round(math.cos(math.radians(angle)), 1)
    return f"Nurk: {angle}, siinus: {sine}, koosinus: {cosine}."


def greetings(n: int) -> str:
    """Return a string that contains "Hey" n times."""
    lots_of_heys = "Hey" * n
    return lots_of_heys


def adding_numbers(num_a: int, num_b: int) -> str:
    """Return given numbers added together as a string."""
    string_numbers = str(num_a) + str(num_b)
    return string_numbers

#if __name__ == "__main__":
    result = time_converter(6500)
    result2 = student_helper(45)
    result4 = adding_numbers(25, 25)
    assert result == "6500 sekundit on 1 tund(i) ja 48 minut(it)."
    assert result2 == "Nurk: 45, siinus: 0.7, koosinus: 0.7."
    assert result4 == "2525"
print(student_helper(45))
print(greetings(3))
print(adding_numbers(25,25))