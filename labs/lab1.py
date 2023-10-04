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

    f = 2 ** (x + 1) - (sin(x - 1)) ** 3

    print("f={0:.4f}".format(f))


def task4():
    a = 5
    alpha = radians(30)
    beta = radians(60)

    abc = (a*sin(alpha)*sin(beta))/2 #произведение высот

    print("{0:.4f}".format(abc))


def task5():
    g = 10
    v0 = float(input("введите занчение="))  # скорость шара
    t = float(input("ведите значение"))  # время падения шара

    h = v0 * t  # высота шара,в момент сбрасывания камня
    v = g * t  # скорость падения шара

    print(h, v)


def task6():
    x1, y1 = 0, 0
    x2, y2 = 3, 0
    x3, y3 = 0, 4

    side1 = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  # сторона треугольника
    side2 = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)  # сторона треугольника
    side3 = sqrt((x1 - x3) ** 2 + (y1 - y3) * 2)  # сторона треугольника

    a = side1 + side2 + side3  # периметр
    b = a / 2  # полупериметр
    s = sqrt(b * (b - side1) * (b - side2) * (b - side3))  # площадь

    print(a, s)


def task7():
    x1 = 3  # координат точки
    x2 = 7  # координата точки

    a = abs(x2 - x1)  # расстояние между точками

    print(a)


def task8():
    S = 20  # расстояние между пунктами
    t1 = 2  # время, за которое катер проходит расстояние

    v1 = S / t1  # скорость катера

    print(v1)


def task9():
    dollars = 100  # Сумма в долларах
    commission_percentage = 2  # Процент комиссии

    # Конвертируем сумму в тенге с учетом комиссии
    tenge = dollars * (1 - commission_percentage / 100)

    # Округляем результат до трех знаков после запятой
    tenge = round(tenge, 3)

    print(tenge)

