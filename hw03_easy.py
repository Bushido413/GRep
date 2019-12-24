# Задание-1:
def my_round(number, ndigits):
    number = number * (10 ** ndigits) + 0.5
    number = number // 1
    number = number / (10 ** ndigits)
    return number

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 6))
print(my_round(2.9999967, 5))


# Задание-2:
def lucky_ticket(ticket_number):
    a = list(map(int, str(ticket_number)))
    list_len = int(len(a)/2)
    if len(a) % 2 == 0:
        if sum(a[:list_len]) == sum(a[list_len:]):
            return "Билет счастливый"
        else:
            return "Билет не счастливый"
    else:
        return "Билет не счастливый"


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
