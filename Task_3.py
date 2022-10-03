# 3. Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.

# Пример:
# 1 -> 2.0
# 2 -> 4.25

n = int(input('Введите число: ')) 

def  numbers(n):

    return[round((1 + 1 / x)**x, 5) for x in range (1, n + 1)]   
        
print(numbers(n))
print(sum(numbers(n)))
