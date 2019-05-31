import math
import random

##Задача 1
x = int(random.randint(1000, 100000))
i = 0
while x > 0:
    if (x % 10) > i:
        i = x % 10
    x //= 10
print(i)

##Задача 2
a = input('a please')
b = input('b please')
print(a, b)

a, b = b, a
print(a, b)

##Задача 3
q = float(input('Введите a'))
w = float(input('Введите b'))
c = float(input('Введите c'))
discr = w ** 2 - 4 * q * c
print('Дискриминант = ', discr)

if discr > 0:
    x1 = (-w + math.sqrt(discr)) / (2 * q)
    x2 = (-w - math.sqrt(discr)) / (2 * q)
    print('x1 = ', x1, 'x2 = ', x2)

elif discr == 0:
    x = -w / (2 * q)
    print('x = ', x)

else:
    print('Корней нет')
# normal is done