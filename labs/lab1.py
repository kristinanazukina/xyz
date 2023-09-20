import math
def task1():
   x=input(float("введи знач:"))
   y=input(float("введи знач:"))
   z=input(float("введи знач:"))
   a=(sqrt(abs(x**3/2)) - math.cos(y))/(1+2*x+math.log(y))
   b=sqrt(x**2/3)-math.cos(y)+z+math.log(y)
print('a=',a)
print('b=',b)
