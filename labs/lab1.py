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

    s = 0.5*abs(x1*(y2-y3) + x2*(y3-y1)+x3*(y1-y2))
    AB = sqrt((x2-x1)**2 + (y2-y1)**2)
