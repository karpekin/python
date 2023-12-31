'''
Task 2
Найдите сумму цифр трехзначного числа.
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
'''

# n = int(input('Введите число: '))
# summa = 0
# while n > 0:
#     x = n%10
#     summa += x
#     n = n//10
# print('Сумма цифр равна:',summa)

'''
Task 4
Петя, Катя и Сережа делают из бумаги журавликов. Вместе
они сделали S журавликов. Сколько журавликов сделал каждый
ребенок, если известно, что Петя и Сережа сделали одинаковое
количество журавликов, а Катя сделала в два раза больше журавликов,
чем Петя и Сережа вместе?
6 -> 1 4 1
24 -> 4 16 4
60 -> 10 40 10
'''
# S = int(input('Сколько всего журавликов?:'))
# # Петя + Сережа + (Петя+Сережа)*2 = S
# # x + x + (x + x)*2 = S
# # x + x + 2x + 2X = S
# # 6x = S
# x = int(S/6)
# print(f'{x} {4*x} {x}')

'''
Task 6
Вы пользуетесь общественным транспортом? Вероятно, вы
расплачивались за проезд и получали билет с номером. Счастливым
билетом называют такой билет с шестизначным номером, где сумма
первых трех цифр равна сумме последних трех. Т.е. билет с номером
385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
программу, которая проверяет счастливость билета.
385916 -> yes
123456 -> no
'''
# number = int(input('Введите шестизнак: '))
#
# sum1 = 0
# sum2 = 0
# n1 = number // 1000
# n2 = number % 1000
#
# while n1 > 0:
#     x1 = n1 % 10
#     x2 = n2 % 10
#     sum1 += x1
#     sum2 += x2
#     n1 = n1 // 10
#     n2 = n2 // 10
#
# print('yes' if sum1 == sum2 else "no")

'''
Task 8
Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
если разрешается сделать один разлом по прямой между дольками 
(то есть разломить шоколадку на два прямоугольника).
'''

# n = int(input('Введите n: '))
# m = int(input('Введите m: '))
# k = int(input('Сколько долек хотите получить?: '))
#
# if n > m:
#     big_side = n
# elif m > n:
#     big_side = m
# else:
#     big_side = m
#
# if k <= big_side and k >= 2:
#     print('yes')
# elif k % n == 0 or k % m == 0:
#     print('yes')
# else:
#     print('no')

# Второй варинт(правильный) 8 задачи
n = int(input('Введите n: '))
m = int(input('Введите m: '))
k = int(input('Сколько долек хотите получить?: '))

if n*m > k:
    if k % n == 0 or k % m == 0:
        print('yes')
    else:
        print('no')
else:
    print('no')
