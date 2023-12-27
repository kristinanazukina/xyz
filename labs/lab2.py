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

def chet(n):
    if n % 2 == 0:
        return True
    else:
        return False
def cub(n):
    if int(n**(1/3)) ** 3 == n:
        return True
    else:
        return False

def task2():
    while True:
        n = float(input("Введите число "))
        if chet(n):
            print(f"{n} оканчивается на чётную цифру")
        else:
            print(f"{n} не оканчивается на чётную цифру")
        if cub(n):
            print(f"{n}куб целого числа")
        else:
            print(f"{n} не куб целого числа")

def decimal_in_new_numeral_system(number,base):
    result = ''
    intp = int(number)
    frp = number - intp
    while intp > 0:
        r = intp % base
        result = str(r) + result
        intp = intp // base
    result += '.'
    pr = 4
    while frp > 0 and pr > 0:
        frp *= base
        digit = int(frp)
        result += str(digit)
        frp -= digit
        pr -= 1
    return result

def task3():
    number = float(input("Введите десятичное число: "))
    base = int(input("Введите систему счисления: "))
    result = decimal_in_new_numeral_system(number,base)
    print(f"Результат: {result}")

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

def task7():
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

def task8():
    s1 = 0 
    for i in range(1,9): 
        for j in range(1, i): 
            s1 += j ** (2 + i) 
    print("1)", s1) 
 
    s2 = 0 
    p2 = 1 
    for i in range(1,9): 
        for j in range(1,4): 
            p2 *= (j + i) 
        s2 += p2 
        p2 = 1 
    print("2)", s2) 
 
    p3 = 1 
    s3_1 = 0 
    s3_2 = 0 
    for i in range(1,9): 
        for j in range(i, (2*i - 1) + 1): 
            for k in range(1, 5): 
                s3_2 += 2*j + 3*i - 0.5*k 
            s3_1 += s3_2 
            s3_2 = 0 
        p3 *= s3_1 
        s3_1 = 0 
    print("3)", p3)

from math import *
def task9():
    x=float(input('введи х:'))
    eps=float(input("введите погрешность:"))

    i=1
    sum=0
    print("аналитическое значение:",round(atan(x),4))

    while (abs(atan(x)-sum)> eps):
        sum += ((-1)**(i))*1/((2*i+1)*(x**(2*i+1)))
        i+=1
        print(i)

    print("Вычисленное значение",round(sum,4))
