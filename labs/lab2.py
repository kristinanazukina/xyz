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


def task2():
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
     def is_happy(number):
         pass
     bilet = int(input("введи номера билета="))
     a1=3
     a2=8
     a3=1
     a4=3
     a5=0
     a6=9
     if a1+a2+a3 == a4+a5+a6:
         print('билет счастливый')
     else:
         print("билет несчастливый")

