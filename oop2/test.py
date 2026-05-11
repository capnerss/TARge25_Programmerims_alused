"""Задание: «Система управления сотрудниками»
Тебе нужно написать небольшую программу для учета сотрудников в компании.

1. Базовый класс Employee (Сотрудник)
Атрибуты:

name (имя)

__salary (приватный атрибут: зарплата)

Методы:

Конструктор __init__, который принимает имя и зарплату.

Геттер get_salary(), который возвращает текущую зарплату.

Метод calculate_bonus(), который по умолчанию возвращает 0.

Метод __str__, который выводит: "Сотрудник: [имя], Зарплата: [зарплата]".

2. Дочерний класс Manager (Менеджер)
Наследуется от Employee.

Добавляет атрибут bonus_amount (фиксированная сумма бонуса).

Переопределяет метод calculate_bonus(), чтобы он возвращал bonus_amount.

Переопределяет __str__, чтобы он добавлял в конце: ", Роль: Менеджер".

3. Дочерний класс Developer (Разработчик)
Наследуется от Employee.

Переопределяет метод calculate_bonus(). Разработчик получает бонус в размере 10% от своей зарплаты.

Переопределяет __str__, чтобы он добавлял в конце: ", Роль: Разработчик".

🚀 Твоя задача:
Реализовать эти три класса.

Создать список employees, в который войдут один Менеджер и один Разработчик.

Пройтись циклом по списку и для каждого сотрудника:

Вывести его описание (сработает __str__).

Вывести размер его бонуса (сработает полиморфизм: у каждого класса своя логика расчета).

💡 Подсказка (если застрянешь):
Для расчета бонуса разработчика внутри класса Developer используй self.get_salary(), так как напрямую к __salary ты обратиться не сможешь из-за инкапсуляции.

Напиши код или спроси, если какой-то пункт вызывает затруднения! Как будешь готов, я пришлю эталонное решение для проверки."""
from django.db.models import manager
from numpy.ma.core import append


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary
    def calculate_bonus(self):
        return 0
    def __str__(self):
        return f"Сотрудник: {self.name}, Зарплата: {self.get_salary}"

class Manager(Employee):
    def __init__(self, name, bonus_amount):
        super().__init__(name)
        self.bonus_amount = bonus_amount
    def calculate_bonus(self):
        return self.bonus_amount
    def __str__(self):
        return f"{super().__str__()}, Роль: Менеджер"

class Developer(Employee):
    def calculate_bonus(self):
        return self.get_salary() * 0.1
    def __str__(self):
        return f"{super().__str__()}, Роль: Разработчик"

employees = []
manager = Manager(name="Kangur", bonus_amount=100)
developer = Developer(name="Juri")
employees.append(manager)
employees.append(developer)
for employee in employees:
    print(employee)
    print(employee.calculate_bonus())

