# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Пример:
# 6782 -> 23
# 0,56 -> 11


print(sum(int (i) for i in input('Введите число:')if i.isdigit()))
