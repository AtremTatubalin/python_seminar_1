'''Задача 6: 
Счастливым билетом называют такой билет с шестизначным номером, 
где сумма первых трех цифр равна сумме последних трех. Т.е. билет с 
номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no'''

number = input("Введите номер билета: ")
number = int(number)
left_tiket = number // 1000
right_tiket = number % 1000
left_summ = 0
right_sum = 0

while (left_tiket > 0):
    num_left = left_tiket % 10
    num_right = right_tiket % 10
    left_summ = left_summ + num_left
    right_sum = right_sum + num_right
    left_tiket = left_tiket // 10
    right_tiket = right_tiket // 10

if (left_summ == right_sum):
    print("yes")
else:
    print("no")