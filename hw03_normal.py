# Задание-1:
def fib(n):
    a = 1
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a


print(fib(10))

# Задание-2:


def sort_to_max(origin_list):
    swap_flag = True
    while swap_flag:
        swap_flag = False
        for i in range(len(origin_list) - 1):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
                swap_flag = True


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задание-3:


def myfilter(func, iterable):
    return [x for x in iterable if func(x) is True]


print(list(myfilter(lambda x: x > 5, [2, 10, -10, 8, 2, 0, 14])))
print(list(filter(lambda x: x > 5, [2, 10, -10, 8, 2, 0, 14])))

# Задание-4:


def is_parallelogram(a1, a2, a3, a4):
    if (a1[0] - a2[0]) == (a3[0] - a4[0]) and\
       (a1[1] - a2[1]) == (a3[1] - a4[1]) and \
       (a4[0] - a3[0]) == (a2[0] - a1[0]) and \
       (a4[1] - a3[1]) == (a2[1] - a1[1]):

        return True
    else:
        return False


a = (1, 1)
b = (2, 2)
c = (3, 3)
d = (4, 4)

print(is_parallelogram(a, b, c, d))
