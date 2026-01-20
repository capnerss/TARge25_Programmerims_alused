"""
Ask for the user's name and age
If the name is shorter than the age or the age is less than 5, greet by name 3 times (Repeat)
Otherwise ask for three numbers and their sum
Report if you got the correct result
"""


def save_user_name_age()->tuple:
    """Take and save age and name from user"""
    name = input("Your name: ")
    age = int(input("Your age: "))
    return name, age


def name_age_compare(name:str, age:int)->bool:
    """
    Compare the age, name length

    If the name is shorter than the age or the age is less than 5, greet by name 3 times (Repeat)
    """


def control_user_sum()->str:
    """Take 3 time input numbers from user and control how he adds the numbers together"""
    first_number = int(input("First number: "))
    second_number = int(input("Second number: "))
    third_number = int(input("Third number: "))
    sum_number = int(input("The sum of three numbers: "))
    control_sum = first_number + second_number + third_number
    if control_sum == sum_number:
        print("Tubli, see on õige vastus!")
        return "Tubli, see on õige vastus!"
    else:
        print(f"Vale vastus, õige oli: {control_sum}")
        return f"Vale vastus, õige oli: {control_sum}"


def user_validator():
    """"""


def name_age():
    """ Küsi kasutaja nime ja vanust
        Kui nime pikkus on väiksem kui vanus või vanus on alla 5 siis tervita nime pidi 3 korda (Kordus)
        Muidu küsi kolm arvu ja nende summa
        Teata kas said õige tulemuse"""
    name = input("Kasutaja nimi: ")
    age = int(input("Kasutaja vanus: "))
    if len(name) < age or age < 5:
        for i in range(3):
            print(f"Tere {name}!")
    else:
        number1 = int(input("Esimine arv: "))
        number2 = int(input("Teine arv: "))
        number3 = int(input("Kolmas arv: "))
        sum_number = int(input("Kolme arvu summa: "))
        controller_sum = (number1 + number2 + number3)
        if controller_sum == sum_number:
            print("Tubli, see on õige vastus!")
        else:
            print(f"Vale vastus, õige oli: {controller_sum}")


if __name__ == '__main__':
    name_age()