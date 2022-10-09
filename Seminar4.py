# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

# str ='-4 -9 8 100'
# lst = str.split(sep=' ')  #по умолчанию сплит пробел вычесляет
# max = min = int(lst[0])
# print(lst)
# for i in range (len(lst)):
#     lst[i] = int (lst[i])
# for i in range (1, len(lst)):
#     if lst[i] > max:
#         max =lst[i]
#     if lst[i]<min:
#         min = lst[i]
# print(f'максимальное число: {max}, минимальное число: {min}')


# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0
# D = b2 – 4ac
#
# a=int(input('введите а: '))
# b=int(input('введите b: '))
# c=int(input('введите с: '))
# d = b**2 - 4*a*c
# print (d)
# if d>0:
#     x1 =(-b + d**0.5)/ (2*a)
#     x2 =(-b - d**0.5)/ (2*a)
#     print (x1, x2)
# elif d==0:
#     x1 = -b/(2*a)
#     print(x1)
# else:
#     print ('такое не возможно')


#3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

# a=int(input('введите а: '))
# b=int(input('введите b: '))
# nod = 2
# while True:                   #бесконечный цикл
#     if b%nod ==0 and a%nod==0:
#         print(nod)
#         break
#     else:
#         nod+=1
# nok = a*b/nod
# print (nok)


