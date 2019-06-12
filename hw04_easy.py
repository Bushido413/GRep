# Задание-1:
import random
lst_r = [random.randint(-10, 10) for _ in range(4)]
print(lst_r)
lst_n = [elem ** 2 for elem in lst_r]
print(lst_n)


# Задание-2:
first_fruits = ['apple', 'orange', 'grape', 'pear', 'watermelon', 'lemon']
second_fruits = ['melon', 'apple', 'peach', 'pear', 'apricot', 'orange']
some_fruits = list(set([fruit for fruit in first_fruits + second_fruits
                        if fruit in first_fruits and fruit in second_fruits]))
print(some_fruits)


# Задание-3:
import random
numbers = [random.randint(-10, 10) for _ in range(10)]
print(numbers)
numbs = [i for i in numbers if i % 3 == 0 and i > 0 and i % 4 !=0]
print(numbs)