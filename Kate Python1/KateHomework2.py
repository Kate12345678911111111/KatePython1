# Задача 1. Для натурального n создать словарь индекс-значение,
# состоящий из элементов последовательности 3n + 1.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# dictionary = {}
# i=1
# n = int(input('введите натуральное число n: '))
# if n <=0:
#     print('Ошибка, введите число >=1')
# else:
#     for i in range(1, n + 1):
#         key = i
#         value = 3 * i + 1
#         dictionary[key] = value
#         i += 1
#     print(f'получен словарь: {dictionary}')


# Задача 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
#
# n = int(input('введите число n'))
# factorial = 1
# for i in range(2, n + 1):
#     factorial *= i
#     print(factorial, end=' ')



# Задача 3. Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.
# Пример:
# - Для n = 5: сумма = 11,55

#
# list = []
# n = int(input('введите число n: '))
# sum = 0
# posledov = 0
# if n <= 0:
#     print('Ошибка, введите число больше 0')
# else:
#     for i in range(1, n + 1):
#         posledov = (1+ (1/i))**i
#         posledov = round(posledov, 2)
#         list.append(posledov)
#         sum = sum + posledov
#         i += 1
#     print(list)
#     print('сумма чисел последовательности (1+ (1/n))^n =', round(sum, 2))



# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

# import random
#
#
# n = int(input('введите число n'))
# lst=[]
# for i in range (-n, n+1):
#     x = random.randint(-n,n)
#     lst.append(x)
# print (lst)
#
# posishn = open ('ввв')
# pos1 = int(posishn.read(1))
# pos2 = int(posishn.read(2))
# posishn.close()
# print(f'позиции из файла: {pos1}, {pos2}')
#
# proizveden = lst[pos1] * lst[pos2]
#
# print(proizveden)

# Подскажите пожалуйста в данной задаче в файле.txt было создано 7 позиций,
# но работает программа только когда задаешь 1 и 2, почему так?


