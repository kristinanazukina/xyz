def task1():
    def chet(num):
        last_digit = int(str(num)[-1])
        return last_digit % 2 == 0

    def is_cube(num):
        root = num ** (1 / 3)
        return round(root) ** 3 == num

    while True:
        user_input = input("введи число( или 'выход'для завершения программмы):")
        if user_input.lower() == "выход":
            break

        try:
            number = int(user_input)

            if chet(number):
                print("число оканчивается на четную цифру")
            else:
                print("число не оканчивается на четную цифру")

            if is_cube(number):
                print("число является кубом целого числа")
            else:
                print("число не является кубом целого числа")

        except ValueError:
            print("Некорректный ввод. пожалуйста,введите целое число")

from math import *
import matplotlib.pyplot as plt

def task2():
    a = int(input('Введите начало диапазона: '))
    b = int(input('Введите конец диапазона: '))
    x_znach = []
    y_znach = []

    def func(a, b):
        x = a
        while x <= b+0.00001:
            if x >= 0:
                result_1 = cos(pi*x)
                y_znach.append(result_1)
            if x < 0:
                result_2 = x**2 +1
                y_znach.append(result_2)
            x_znach.append(x)
            x += 1
        return x_znach, y_znach
    print(func(a, b))
    plt.plot(x_znach, y_znach)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График функции')
    plt.grid(True)
    plt.show()


def task3():
    def number_in_new_numeral_system(number, base):
        if base < 2 or base > 16:  # Проверяем, что выбранное основание находится в допустимом диапазоне
            return "Ошибка: Недопустимое основание системы счисления"

        if number == 0:
            digits = "0123456789ABCDEF"  # Цифры, используемые в различных системах счисления

            result = ""
            negative = False
        if number < 0:  # Проверяем, является ли число отрицательным
            negative = True
        number = abs(number)

        while number > 0:
            remainder = number % base  # Остаток от деления числа на основание новой системы счисления
        result = digits[remainder] + result
        number = number // base  # Целая часть от деления числа на основание новой системы счисления

        if negative:
            result = "-" + result  # Если число было отрицательным, то добавляем знак "-" к результату

        return result

    # Пример использования функции
    number = int(input("Введите число в десятичной системе счисления: "))
    base = int(input("Введите основание новой системы счисления: "))
    result = number_in_new_numeral_system(number, base)
    print(f"Число {number} в системе счисления с основанием {base} равно {result}")

    return "0"  # Если число равно нулю, то возвращаем строку "0"


def task5():
    # Функция для вычисления суммы цифр числа
    def sum_of_digits(number):
        return sum(int(digit) for digit in str(number))

    # Три заданных трехзначных числа
    numbers = [123, 456, 789]

    # Заданное значение суммы цифр
    m = 10

    # Вывод четных чисел, сумма цифр которых больше m
    for number in numbers:
        if len(str(number)) == 3 and number % 2 == 0 and sum_of_digits(number) > m:
            print(number)

def task6():
    def is_happy():
        bilet = int(input("введи номера билета="))
        bilet = str(bilet)
        a1 = int(bilet[0])
        a2 = int(bilet[1])
        a3 = int(bilet[2])
        a4 = int(bilet[3])
        a5 = int(bilet[4])
        a6 = int(bilet[5])
        if a1 + a2 + a3 == a4 + a5 + a6:
            print('билет счастливый')
        else:
            print("билет несчастливый")
    is_happy()

def task8():
    def calculate_sum(epsilon):
        term = 1
        sum = term
        n = 1
        while abs(term) > epsilon:
            term = (-1) ** n * (1 - n)
            sum += term
            n += 1
        return sum

    epsilon = 0.0001
    result = calculate_sum(epsilon)
    print(f"сумма членов ряда с точностью до {epsilon} равна: {result}")
import matplotlib.pyplot as plt

def task4():
    x1=[-7,-6,-2,-4,1,-7]
    y1=[5,-4,-6,0,4,5]
    axes=plt.subplot()
    axes.plot(x1,y1,color='black')
    axes.set_aspect(1)

    x2=[1,1,3,5,6,3,1]
    y2=[-7,-2,-1, 2,-3,-4,-7]
    axes.plot(x2, y2, color='black')
    plt.grid()
    plt.title('Task 4')
    plt.show()
