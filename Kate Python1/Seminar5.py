# 1. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


# import math
#
# num = float(input('Введите число от 10^{-10} до 10^{-1}: '))
# count = 0
# if num >= 10 ** (-10) and num <= 10 ** (-1):
#     while (num != 1):
#         num *= 10
#         count += 1
#     x = str(round(math.pi, count + 1))
#     print(f'Число π с соответствующим количеством знаков = {x[:(len(x) - 1)]}')
#     print(f'Число π = {math.pi}')
#
# else:
#     print('Ошибка!Введите число от 10^{-1} до ≤10^{-10}')

#
# from math import pi
#
# d = float(input())
# d = len(str(d))
# print (str(d))
# print(str(pi)[:d])



# 2. Задайте натуральное число N. Напишите программу, которая
# составит список простых множителей числа N.


n = input('введите натуральное число:  ')
print('\nTask2')

def prime_factors(n):
   i = 2
   lst_prime = []
   while i * i <= n:
       while n % i == 0:
           lst_prime.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       lst_prime.append(int(n))
   return lst_prime

num2 = int(input('Input Number :'))
print(prime_factors(num2))


#
# 3. Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.


# import random
#
# list = []
# for i in range(10):
#     list.append(random.randint(1, 10))
# print(list)
#
# list2 = []
#
# count = 0
# for i in list:
#     if list.count(i) == 1:
#         list2.append(i)
#
# print(list2)

# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного,
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число. 0 1 2 3 4 6 7 8

# with open('file.txt', 'r') as f:
#     lst = list(map(int, f.read().split(' ')))
#
#
#     for i in range (1, len(lst)):
#         if lst[i]  != lst[i-1] +1:
#             lst.insert(i, lst[i]-1)
#
# print(lst)
# with open('file.txt', 'w') as f:
#     f.write(' '.join(map(str, lst)))



# Напишите программу, удаляющую из текста все слова, содержащие "абв".

# str = 'забвение мой абвернатор'
# list = filter str.split(' ')
# print(list)

