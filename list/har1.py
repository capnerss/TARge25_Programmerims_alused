"""
Har1.
"""

from random import randint


def generate_number_list(smallest: int, lagrest: int) -> list[int]:
    result = []
    for i in range(10):
        random_number = randint(smallest,lagrest)
        result.append(random_number)
    return result


def ask_user(question: str)->int:
    user_input = input(question)
    while not user_input.isdigit():
        print("Input erorr")
        user_input = input(question)
    return int(user_input)


def multy_list(numbers, multiplair):
    result = []
    for number in numbers:
        result.append(number * multiplair)
    return result


def show_result(original_numbers, multiplier, resulting_numbers):
    for i in range(len(original_numbers)):
        print(f"{original_numbers[i]} * {multiplier} = {resulting_numbers[i]}")



if __name__ == '__main__':
    number_list = generate_number_list(1,10)
    multiplier = ask_user("Please insert multiplier")
    multiplayed = multy_list(number_list, multiplier)
    show_result(number_list, multiplier, multiplayed)

