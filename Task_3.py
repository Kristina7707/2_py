# 3. Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.

# Пример:
# 1 -> 2.0
# 2 -> 4.25


n = int(input())

numbers = []

for i in range(0, n):
    input_value = int(input(f'Введите число n {i}: '))
    numbers.append(input_value)

sum = 0
for i in numbers:
    sum += i

print('Сумма всех чисел последовательности:', sum)