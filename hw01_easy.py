import random

##Задача 1
x = str(random.randint(1000, 100000))
i = 0
print("Random number is", x)
while i < len(x):
    print(x[i])
    i += 1

##Задача 2
a = input('a please')
b = input('b please')
o = int()
print(a, b)

o = a
a = b
b = o
print(a, b)

##Задача 3
age = input('age please')
if int(age) >= 18:
    print('good')
else:
    print('bad')
# easy is done