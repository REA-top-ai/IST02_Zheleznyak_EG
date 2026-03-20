import datetime

from matplotlib.pyplot import plot_date

current_time = datetime.datetime.now()
print(current_time)


import random

random_list = [random.randint(1, 100) for number in range(101)]
random_number = random.choice(random_list)

print(random_number)


import matplotlib.pyplot as plt
import random

number_a = range(1, 13)
number_b = random.sample(range(1000), 12)

plt.plot(number_a, number_b)
plt.show()

from datetime import datetime

employees = [
    ["Иванов Иван Иванович", "Менеджер", "22.10.2013", 250000],
    ["Сорокина Екатерина Матвеевна", "Аналитик", "12.03.2020", 75000],
    ["Стуков Иван Сергеевич", "Старший программист", "23.04.2012", 150000],
    ["Корнеева Анна Игоревна", "Ведущий программист", "22.02.2015", 120000],
    ["Старчиков Сергей Анатольевич", "Младший программист", "12.11.2021", 50000],
    ["Бутенко Артем Андреевич", "Архитектор", "12.02.2010", 200000],
    ["Савченко Алина Сергеевна", "Старший аналитик", "13.04.2016", 100000]
]


def programmer_bonus():
    for emp in employees:
        if "программист" in emp[1]:
            bonus = emp[3] * 0.03
            print(f"{emp[0]} - премия ко дню программиста: {bonus} руб.")


def gender_bonus():
    for emp in employees:
        name_parts = emp[0].split()
        patronymic = name_parts[2] if len(name_parts) > 2 else ""

        if patronymic.endswith("вна"):
            print(f"{emp[0]} - премия к 8 марта: 2000 руб.")
        else:
            print(f"{emp[0]} - премия к 23 февраля: 2000 руб.")


def salary_indexation():
    current_date = datetime.now()

    for emp in employees:
        hire_date = datetime.strptime(emp[2], "%d.%m.%Y")
        years_worked = (current_date - hire_date).days / 365.25

        if years_worked > 10:
            indexation = emp[3] * 0.07
        else:
            indexation = emp[3] * 0.05

        new_salary = emp[3] + indexation
        print(f"{emp[0]} - индексация: {indexation} руб., новая зарплата: {new_salary} руб.")


def vacation_schedule():
    current_date = datetime.now()
    vacation_list = []

    for emp in employees:
        hire_date = datetime.strptime(emp[2], "%d.%m.%Y")
        months_worked = (current_date - hire_date).days / 30.44

        if months_worked > 6:
            vacation_list.append(emp[0])

    print("Сотрудники, отработавшие более 6 месяцев:")
    for emp in vacation_list:
        print(emp)


print("Премия ко дню программиста")
programmer_bonus()
print("\nПремия к 8 марта и 23 февраля")
gender_bonus()
print("\nИндексация зарплат")
salary_indexation()
print("\nГрафик отпусков")
vacation_schedule()


import random

def find_winners():
    admin_number = random.randint(1, 9)
    print(f"Загаданное число администрации: {admin_number}")

    players = []
    num_players = int(input("Введите количество участников: "))

    for i in range(num_players):
        player_number = int(input(f"Введите число игрока {i + 1}: "))
        players.append(player_number)

    winners = []

    for player_num in players:
        if len(winners) >= 5:
            break

        digit_sum = sum(int(digit) for digit in str(abs(player_num)))

        if digit_sum % admin_number == 0:
            winners.append(player_num)

    print("\nВыигрышные номера:")
    if winners:
        for winner in winners:
            print(winner)
    else:
        print("Нет выигрышных номеров")

find_winners()


import random

# Задание 1: Броски монеты
def coin_flips():
    n = int(input("Введите количество бросков монеты: "))
    for _ in range(n):
        result = random.choice(["Орел", "Решка"])
        print(result)

# Задание 2: Броски кубика
def dice_rolls():
    n = int(input("Введите количество бросков кубика: "))
    for _ in range(n):
        result = random.randint(1, 6)
        print(result)

# Задание 3: Генерация пароля
def generate_password():
    length = int(input("Введите длину пароля: "))
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    password = ""
    for _ in range(length):
        password += random.choice(alphabet)
    print(f"Сгенерированный пароль: {password}")

print("Задание 1: Броски монеты")
coin_flips()
print("\nЗадание 2: Броски кубика")
dice_rolls()
print("\nЗадание 3: Генерация пароля")
generate_password()