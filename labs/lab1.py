from math import *
x = float(input("Введите значение переменной x "))
y = float(input("Введите значение переменной y "))
z = float(input("Введите значение переменной z "))
a=(sqrt(abs(x**3/2))-cos(y))/(1+2*x+log(y))
b=sqrt(x**2/3)-cos(y)+ z+ log(y)
print("Значение a = ", a, "Значение b = ", b)


