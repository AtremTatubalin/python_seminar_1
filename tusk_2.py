'''Задача 2: Найдите сумму цифр трехзначного числа.'''

number = input("Введите число: ")
number = int(number)
summa = 0
while (number > 0):
    a = number % 10
    summa = summa + a
    number = number // 10
print(f"Сумма цыфр равна: {summa}")
