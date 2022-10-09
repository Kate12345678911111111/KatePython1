# 1. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# from math import pi
#
# d = float(input())
# d = len(str(d))
# print (str(d))
# print(str(pi)[:d])


# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


# n = int(input("введите натуральное число: "))
# factors = []
# d = 2
# m = n                                                       # Запомним исходное число
# while d * d <= n:
#         if n % d == 0:
#             factors.append(d)
#             n//=d
#         else:
#             d += 1
# factors.append(n)                                           # Добавим последнеё простое число
# print('{} = {}' .format(m, factors))                        # Выводим исходное число и все простые множители.


#
# 3. Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.
#
# import random
#
# list = []
# for i in range(10):
#     list.append(random.randint(1, 10))
# print(list)
#
# list2 = []
#
# for i in list:
#   if i not in list2:
#       list2.append(i)
#
# print(list2)
#
