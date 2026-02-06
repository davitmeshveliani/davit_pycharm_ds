# #Спрашиваем у пользователя число
# x= int(input("Введите высоту лестницы"))
# # Начинаем с верха
# for i in range(x,0,-1):
#     # Печатаем i
#     print("*" * i)

#weilistvis kaia
# for i in range(x):
#     print("*"*x)
#     x -= 1
#-----------------------
# # brayk it
# text = input("Введите текст ")
# in_ASCII = True
# for letter in text:
#     if ord(letter) > 127:
#         in_ASCII = False
#         break
# print("Все символы ASCII: ", in_ASCII)

#-----------------
# Проверка скобок
# Задание: Напишите программу, которая проверяет правильность расстановки круглых скобок в строке.
#
#
# Пример вывода:
# Введите строку: (a+b)*(c-d)
# Скобки расставлены правильно? True
#
#
# Введите строку: (a+b)(*((c-d)
# Скобки расставлены правильно? False
# start =  int(input("Введите начальный код: "))
# end = int(input("Введите конечный код: "))
#
# result = ""
# for code in range(start, end + 1):
#     result += chr(code)
#
# print("Символы: ", result)
#-----------
# Строка из диапазона Unicode
# Напишите программу, которая принимает два числа
# (начало и конец диапазона Unicode) и выводит строку,
# состоящую из всех символов этого диапазона.
#
# Пример вывода:
# Введите начальный код: 65
# Введите конечный код: 70
# Символы: ABCDEF

# start =  int(input("Введите начальный код: "))
# end = int(input("Введите конечный код: "))
#
# result = ""
# for code in range(start, end + 1):
#     result += chr(code)
#
# print("Символы: ", result)

# n = int(input("Введите число: "))# davaleba n=9 .1#
#
# max_num = n * n
# width = len(str(max_num)) + 1
#
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         s = str(i * j)
#         print(" " * (width - len(s)) + s, end="")
#     print()
#----------   9.1/2
# n = int(input("Введите число: "))
#
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(f"{i*j:4}", end="")
#     print()

#------------9.-2
# n = int(input("Введите число: "))
#
# for i in range(1, n + 1):       # ციკლი 1-დან n-მდე
#     for j in range(1, i + 1):   # შიდა ციკლი 1-დან i-მდე — ანუ თითოეულ სტრიქონში შესაბამისი რაოდენობის რიცხვი
#         print(j, end="")        # რიცხვის დაბეჭდვა ერთ ხაზზე
#     print()                     # ხაზის გადატანა ახალი სტრიქონზე
#

#---------9.-3
# text = input("Введите строку: ")
# result = ""
#
# for letter in text:
#     if letter not in result:
#         result += letter
#
# print("Результат:", result)

# text = input("Введите строку: ")
# result = ""
#
# for char in text:
#     if char not in result:
#         result += char
#
# print("Результат:", result)
















