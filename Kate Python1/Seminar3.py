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

# if number >=1:
#     while i<=number:
#         key=i
#         val=3*i+1
#         dictionary[key]=val
#         i+=1
# else:
#     print ('ошибка')
# print(f'получен словарь: {dictionary}')


# Задача 3. Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.
# Пример:
# - Для n = 5: сумма = 11,55

# n = int(input('введите число n'))
# a = int(input("Введите число N: "))
# i = 0
# x = 0
# lst = []
# while i <= a - 1:
#     i += 1
#     b = (1 + (1 / i)) ** i
#     lst.append(b)
#     x = x + b
# print("Список последовательных чисел числа N:", lst)
# print("Сумма последовательных чисел числа N по формуле (1+ (1/n))^n равна", round(x, 2))



# Напишите программу, в которой пользователь будет
# задавать две строки, а программа -
# определять количество вхождений одной строки в другой.

# str1 = 'Привет, как у вас дела Привет'
# str2 = 'Привет'
#
# lst = str1.split(sep=' ')
# print(lst)
# count = 0
# for i in range (len(lst)):
#     if lst[i]==str2:
#         count+=1
# print(count)


# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1


# list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу", "йцу"]
# str = 'йцу'
# count = 0
# for i in range (len(list)):
#     if list[i] == str:
#         count +=1
#     if count ==3:
#         print(i)
#         break
# if count !=2:
#     print(-1)