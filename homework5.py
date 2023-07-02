'''
Задача 26: Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
'''
'''1-й Вариант'''
# A, B = int(input('Введите A: ')), int(input('Введите целое B: '))
# def pow1(a, b):
#     if b < 0:
#         return 1 / pow1(a, -b)
#     elif b == 0:
#         return 1
#     else:
#         return a*pow1(a, b - 1)
# print(pow1(A, B))

'''2-й Вариант'''
# A, B = int(input('Введите A: ')), int(input('Введите целое B: '))
# def pow2(a, b):
#     if b == 0:
#         return 1
#     elif b < 0:
#         return 1 / pow2(a, -b)
#     elif b % 2 == 0:
#         c = pow2(a, b // 2)
#         return c * c
#     else:
#         return a * pow2(a, b - 1)
# print(pow2(A, B))

'''
1. Если exponent равен 0, функция возвращает 1, поскольку любое число, возведенное в степень 0, равно 1.
2. Если exponent меньше 0, функция вызывает себя с противоположным знаком показателя степени и возвращает обратное значение результата. Это позволяет обрабатывать отрицательные степени.
3. Если exponent является четным числом, функция рекурсивно вызывает себя для половины показателя степени и возвращает квадрат этого значения. Это основано на свойстве a^(2b) = (a^b)^2.
4. Если exponent является нечетным числом, функция рекурсивно вызывает себя для показателя степени минус один, а затем умножает результат на основание. Это основано на свойстве a^(b+1) = a * a^b.
'''

'''
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму 
двух целых неотрицательных чисел. Из всех арифметических операций 
допускаются только +1 и -1. Также нельзя использовать циклы.
*Пример:*
2 2
4
'''
# A, B = int(input('Введите целое положительное A: ')), \
#     int(input('Введите целое положительное B: '))

'''1-й Вариант'''
# def sum1(a, b):
#     if a == 0:
#         return b
#     elif b == 0:
#         return a
#     else:
#         return sum1(a - 1, b) + 1
#
#
# print(sum1(A, B))

'''2-Вариант'''
A, B = int(input('Введите целое положительное A: ')), \
    int(input('Введите целое положительное B: '))


def sum1(a, b):
    if a == b:
        return a + b
    elif a < b:
        return sum1(a, b-1) + 1
    else:
        return sum1(a-1, b) + 1


print(sum1(A, B))