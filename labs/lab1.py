from math import *
x = float(input("Введите значение переменной x "))
y = float(input("Введите значение переменной y "))
z = float(input("Введите значение переменной z "))
a=(sqrt(abs(x**3/2))-cos(y))/(1+2*x+log(y))
b=sqrt(x**2/3)-cos(y)+ z+ log(y)
print("Значение a = ", a, "Значение b = ", b)

#task2
from math import *
x=float(input("введите значение переменной="))
a=2
b=-1
f=((sqrt(x))/(sqrt(x+a))) + x**b
print('f=',f)

#task3
from math import *
x=float(input("введите значение="))
f=2**(x+1) -(sin(x-1))**3
print('f=',f)

