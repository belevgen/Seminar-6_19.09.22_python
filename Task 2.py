# первоначально:
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11


# a = str(input('Введите число: '))
# sum = 0
# for i in a:
#    if i.isdigit():
#        sum = sum + int(i)
# print(sum)

# улучшенный вариант:
from functools import reduce

n = input("Введите вещественное число: ").replace(',', '')
m = list(map(int, n))
print(f'Сумма цифр числа равна', reduce(lambda x, y: x + int(y), m))