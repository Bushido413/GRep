# Задача-1:
fruits = ['apple', 'banana', 'mango', 'pear', 'pineapple']
i = 1
for n in fruits:
    print('{0}. {1}'.format(i, n.rjust(10)))
    i += 1

# Задача-2:
first = [4, 8, 15, 16, 23, 42]
second = [2, 4, 6, 8, 10, 12, 14, 16]
first = [x for x in first if x not in second]
print(first)

# Задача-3:
numbers = {1, 7, 9, 20, 35, 64, 68, 122}
numbers_second = []
for m in numbers:
    if m % 2 == 0:
        numbers_second.append(m / 4)
    else:
        numbers_second.append(m * 2)
print(numbers_second)
