# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
#
# import random                               # случайный список
#
# lst = []
# for i in range (random.randint(1, 10)):   #сколько чисел в списке
#     x = random.randint(-10,10)           # какие числа в списке
#     lst.append(x)
# random.shuffle(lst)                        #перемешивание элементов в списке
# print(lst)
# sum = 0
# for i in range (len(lst)):
#     if i % 2 != 0:                          # проверка на четность
#         sum += lst[i]
#         i += 1
# print(f'сумма элементов списка, стоящих на нечётной позиции: {sum}')                                     #



# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# import random
# lst = []
# for i in range (random.randint(1, 10)):   #сколько чисел в списке
#     x = random.randint(-10,10)           # какие числа в списке
#     lst.append(x)
# random.shuffle(lst)                        #перемешивание элементов в списке
# print(lst)
# for i in range (len(lst)):
#     length = i+1
# print (f'Длинна списка: {length}')
# midlst = length//2
# if length % 2 == 0:
#     while length !=midlst:
#         for i in range (0, midlst):
#             proizved = lst[i]*lst[length-1]
#             length-=1
#             i+=1
#             print(proizved)
# else:
#     while length != midlst:
#         for i in range(0, midlst+1):
#             proizved = lst[i] * lst[length - 1]
#             length -= 1
#             i += 1
#             print(proizved)

# вар 2
# from random import randint
# array_size = int(input("Введите сколько чисел должно быть в списке: "))
# lst1 = []
# for i in range(array_size):
#     lst1.append(randint(1, 10))
# print("Заданный список рандомных чисел:", lst1)
# lst_multiplied = []
# ln = len(lst1)
# for i in range(ln):
#     if i >= ln/2:
#         break
#     print(lst1[i] * lst1[-i-1], end=' ')




# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# import random
#
# lst = []
# for i in range (random.randint(1, 10)):
#     x = random.random()*10
#     lst.append(round(x,1))
# random.shuffle(lst)
# print(lst)


# lst = [1.1, 1.2, 3.1, 5.03, 10.1]
#
# drobChast=0                                    #lst[i]*10%10
# differ = 0
# list1=[]
# for i in range (len(lst)):
#     drobChast = lst[i]* 10 % 10
#     list1.append((drobChast)/10)
# print(list1)
# max = min = list1[0]
# for j in range (len(list1)):
#     if list1[j] > max:
#         max =list1[j]
#     if list1[j]<min:
#         min = list1[j]
#     j += 1
# print(f'максимальная дробная часть: {max}')
# print(f'минимальная дробная часть: {min}')
# differ = max-min
# print(f'разница между максимальным и минимальным значением дробной части элементов: {differ}')


#
# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
#

# a = int(input('Введите число: '))
# b = '' # остатки от деления на 2
# while a>0:
#     b = str(a%2)+b
#     a = a//2
# print(b)

# Второй вариант
# a = int(input('Введите число: '))
# print(bin(a))

# n = int(input())
# print('{0:b}'.format(n))



# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
#
# fib1 = fib2 = 1
#
# n = int(input())
#
# print(fib1, fib2, end=' ')
#
# for i in range(2, n):
#     fib1, fib2 = fib2, fib1 + fib2
#     print(fib2, end=' ')

# n = int(input('Введите число: '))

# def get_fibonacci(n):
#     fibo_nums = []
#     a, b = 1, 1
#     for i in range(n+1-1):
#         fibo_nums.append(a)
#         a, b = b, a + b
#     a, b = 0, 1
#     for i in range (n+1):
#         fibo_nums.insert(0, a)
#         a, b = b, a - b
#     return fibo_nums
#
# fibo_nums = get_fibonacci(n)
# print(get_fibonacci(n))

# вар 2
# print('\nTask5')
#
# def neg_fibonach(num, j):
#     return num * (-1) ** (j + 1)
#
# fib1 = 0
# fib2 = 1
# lst5 = []
# lst_neg = []
# lst5.append(fib1)
# lst5.append(fib2)
# lst_neg.append(neg_fibonach(fib1, 0))
# lst_neg.append(neg_fibonach(fib2, 1))
#
# k = int(input('Введите номер элемента ряда Фибоначчи: '))
#
# for i in range(k - 1):
#     fib1, fib2 = fib2, fib1 + fib2
#     lst5.append(fib2)
#     lst_neg.append(neg_fibonach(fib2, i))
#
# print(lst5)  # check
# print(lst_neg)  # check
#
# lst_sum = []
# for i in range(k):
#     lst_sum.append(lst_neg[-i - 1])
#     # разворот негафибоначчи и внесение в суммарный список
#
# for i in range(k + 1):
#     lst_sum.append(lst5[i])
#     # добавление нормального ряда фибоначчи
#
# print(lst_sum)
