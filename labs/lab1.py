from math import *
def task1():
    x = float(input("Введите значение переменной x "))
    y = float(input("Введите значение переменной y "))
    z = float(input("Введите значение переменной z "))

    a = (sqrt(abs(x ** 3 / 2)) - cos(y)) / (1 + 2 * x + log(y))
    b = sqrt(x ** 2 / 3) - cos(y) + z + log(y)

    print("{0:.4f}".format(a, b))


def task2():
    x = float(input("введите значение переменной="))
    a = 2
    b = -1

    f = ((sqrt(x)) / (sqrt(x + a))) + x ** b

    print("f={0:.4f}".format(f))


def task3():
    x = float(input("введите значение="))

    f = 2  (x + 1) - (sin(x - 1))  3

    print("f={0:.4f}".format(f))

def task4():
    a = 5
    alpha = radians(30)
    beta = radians(60)

    s = (a + a + a) / 2 # Полупериметр
    R = (a * a * a) / (4 * sqrt(s * (s - a) * (s - a) * (s - a)))

    #вычисляем длины высот
    h_alpha = (2 * R * sin(alpha))
    h_beta = (2 * R * sin(beta))

    # Вычисляем произведение высот
    abc = h_alpha * h_beta

    print("{0:.4f}".format(abc))


def task5():
    g = 10
    v0 = float(input("введите занчение="))
    t = float(input("ведите значение"))

    h = v0 * t
    v = g * t

    print(h, v)


def task6():
    x1, y1 = 0, 0
    x2,y2 = 3,0
    x3,y3 = 0,4

    side1 = sqrt((x2 - x1)  2 + (y2 - y1)  2)
    side2 = sqrt((x3 - x2)  2 + (y3 - y2)  2)
    side3 = sqrt((x1 - x3)  2 + (y1 - y3)  2)

    a = side1 + side2 + side3 #периметр
    b = a / 2 #полупериметр
    s = sqrt(b * (b- side1) * (b - side2) * (b- side3)) #площадь

    print(a, s)


def task7():
    x1 = 3
    x2 = 7

    a = abs(x2 - x1)

    print(a)

def task8():
    S = 20
    t1 = 2

    v1 = S / t1

    print(v1)

def task9():
    dollars = 100  # Сумма в долларах
    commission_percentage = 2  # Процент комиссии

    # Конвертируем сумму в тенге с учетом комиссии
    tenge = dollars * (1 - commission_percentage / 100)

    # Округляем результат до трех знаков после запятой
    tenge = round(tenge, 3)

    print(tenge)