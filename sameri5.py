# import math  # აუცილებელია ეს სტრიქონი
# num = float(input("შეიყვანე რიცხვი: "))
# print("კვადრატული ფესვი არის:", math.sqrt(num))

# import math
# input = "sheiyvane ricxvi"
# print(int(input(math.sqrt(16))))
# import math
#
# num = float(input("შეიყვანე რიცხვი: "))
# print(int(math.sqrt(num)))

# davaleba 1
# # Запрос числа у пользователя и преобразование в целое число
# number = int(input("Введите число: "))
#
# # Берём абсолютное значение, чтобы работать и с отрицательными числами
# number = abs(number)
#
# # Начальная сумма цифр = 0
# digit_sum = 0
#
# # Пока число больше 0, извлекаем каждую цифру
# while number > 0:
#     digit = number % 10         # Последняя цифра числа
#     digit_sum += digit          # Прибавляем к общей сумме
#     number = number // 10       # Удаляем последнюю цифру
#
# # Выводим результат
# print("Сумма цифр:", digit_sum)

#####
# total = 0
#
# while True:
#     number = int(input("Введите число: "))
#     if number == 0:
#         break
#     if number > 0:
#         total += number
#
# print("Общая сумма положительных:", total)


# b = 0
# while True:
#     a = float(input("число>: "))
#     if a == 0:
#         print(b)
#         break
#     if a < 0 :
#         continue
#     b += a

# b = 0
# a = 1
# while a :
#     a = float(input("число>: "))
#     if a > 0 :
#         b += a
# print(b)

# import random
#
# secret = random.randint(1, 10)
#
# for attempt in range(5, 0, -1):
#     guess = int(input("Угадайте число от 1 до 10: "))
#
#     if guess == secret:
#         print("Поздравляем! Вы угадали число.")
#         break
#     else:
#         if guess < secret:
#             hint = "Слишком мало!"
#         else:
#             hint = "Слишком много!"
#
#         if attempt - 1 > 0:
#             print(f"{hint} У вас осталось {attempt - 1} попыток.")
#         else:
#             print(f"{hint} Вы проиграли! Загаданное число было: {secret}")

# import random
# p = 5
# rann = random.randint(1, 5 )
# while p > 0:
#     p -= 1
#     num = int(input("Попробуйте угадать число от 1 до 10 :"))
#     if num == rann:
#         print("Поздравляем! Вы угадали число.")
#         break
#     print("Неверно! У вас осталось", p, "попытки.")
# else:
#     print("Число было :", rann)

########
# n = int(input("Введите количество чисел: "))
#
# n = int(input("Введите количество чисел: "))
#
# a, b = 0, 1
# count = 0
#
# while count < n:
#     print(a, end=" ")
#     a, b = b, a + b
#     count += 1

####
# num = int(input("Введите количество чисел: "))
# num1 = 0
# num2 = 1
# count = 0
# while count < num:
#     count +=1
#     print(num1)
#
#num = num, num2 + num1
#############################
# num = input("Введите число: ")
#
# if num == num[::-1]:
#     print("Число является палиндромом.")
# else:
#     print("Число не является палиндромом.")
################################
# num = input("Введите число: ")
# if list(num) == list(reversed(num)):
#     print("Число является палиндромом.")
# else:
#     print("Число не является палиндромом.")

#########  davaleba 8

# char = input("Введите символ: ")
# code = ord(char)
# print("Код Unicode:", code)
# print("ASCII символ:", code <128)

######################

# text = input("Введите строку: ")
# start = int(input("Введите начальный индекс: "))
# end = int(input("Введите конечный индекс: "))
# substring = text[start:end]
# missing = max(0, end - len(text))
# substring += "_" * missing
# print("Подстрока:", substring)
##//////////////////////*****************************
# text = input("Введите строку: ")
# char = input("Введите символ: ")
#
# if len(char) != 1:
#     print("Ошибка: введите только один символ.")
# else:
#     print("Символ '" + char + "' встречается " + str(text.count(char)) + " раз(а).")

###////////////////////////////////
# 1)
#
# char = input("Введите символ: ")
# code = ord(char)
# print("Код Unicode:", code)
# print("ASCII символ:", code < 128)
#
# 2)
# text = input("Введите строку: ")
# start = int(input("Введите начальный индекс: "))
# end = int(input("Введите конечный индекс: "))
# substring = text[start:end]
# missing = max(0, end - len(text))
# substring += "_" * missing
# print("Подстрока:", substring)
#
# 3)
# text = input("Введите строку: ")
# char = input("Введите символ: ")
#
# if len(char) != 1:
#     print("Ошибка: введите только один символ.")
# else:
#     print("Символ '" + char + "' встречается " + str(text.count(char)) + " раз(а).")
#-------------------

# ----------leqsia koleqcia------------

#------------------------------------------
#---pithon 19-------

# text = input("Введите строку: ")
# char = input("Введите символ: ")
#
# if len(char) != 1:
#     print("Ошибка: введите только один символ.")
# else:
#     count = 0
#     i = 0
#     while i < len(text):
#         if text[i] == char:
#             count += 1
#         i += 1
#     print("Символ '" + char + "' встречается " + str(count) + " раз")
# Напишите программу, которая изменяет изначальный список и возводит в квадрат только нечётные числа.
#
# numbers = [4, 9, 1, 7, 2, 5, 0, 3, 7, 1, 3]
#
# Пример вывода:
#
# Изначальный список: [4, 9, 1, 7, 2, 5, 0, 3, 7, 1, 3]
#
# Измененный список:  [4, 81, 1, 49, 2, 25, 0, 9, 49, 1, 9]


# my_list = [4, 9, 1, 7, 2, 5, 0, 3, 7, 1, 3]
#
# print("Изначальный список:", my_list)
#
# for i in range(len(my_list)):
#     if my_list[i] % 2 != 0:
#         my_list[i] = my_list[i] ** 2
#
# print("Измененный список:", my_list)


# სია სხვადასხვა რიცხვებით
# my_list = [4, 9, 1, 7, 2, 5, 0, 3, 7, 1, 3]
#
# print("Изначальный список:", my_list)  # დაბეჭდეთ თავდაპირველი სია
#

# შემოვლით ციკლი ინდექსებით, რათა შეგვეძლოს სიის ელემენტების შეცვლა ადგილზე
# for i in range(len(my_list)):
#     # შემოწმება, თუ რიცხვი კენტია
#     if my_list[i] % 2 != 0:
#         # თუ კენტია, ვადიდებთ მისი კვადრატით
#         my_list[i] = my_list[i] ** 2
#
# print("Измененный список:", my_list)

###############################################################
#
# import random
#
# secret = random.randint(1, 100)
# attempts = 0
#
# print("Угадайте число от 1 до 100. У вас 10 попыток.")
#
# while attempts < 10:
#     guess = int(input("Ваше предположение: "))
#     attempts += 1
#
#     if guess < secret:
#         print("Загаданное число больше вашего.")
#     elif guess > secret:
#         print("Загаданное число меньше вашего.")
#     else:
#         print("Поздравляем! Вы угадали число: за попыток.")
#         break
# else:
#     print("Вы не угадали. Загаданное число было:")

# current_hours = 22
# hours = 3
# end_time = current_hours + 3
#
# while current_hours < 24 and current_hours < end_time:  # Внешний цикл с использованием while
#     for minutes in range(5):  # Внутренний цикл с использованием for
#         print("Время (часов:минут): ", current_hours, ':', minutes, sep='')
#     current_hours += 1  # Увеличение значения часов на 1




###########========
# text = input("Введите строку: ")
# symbol = input("Введите символ: ")
#
# count = 0
#
# for letter in text:
#     if letter == symbol:
#         count = count + 1
#
# print("Символ", symbol, "встречается", count, "раз.")

#
# text = input("Введите строку: ")
# result = ""
# for letter in text[::-1]:
#     if letter not in "0123456789":
#         result = result + letter
# print(result)

# numbers = [4, 9, 1, 7, 2, 5, 0, 3, 7, 1, 3]
#
# print("Изначальный список:", numbers)
#
# for i in range(len(numbers)):
#     if not numbers[i] % 2 == 0:
#         numbers[i] = numbers[i] ** 2
#
# print("Измененный список:", numbers)
##3---------------------------------------
# # Доступные номиналы монет
# coins = [50, 10, 5, 2, 1]
#
# # Ввод стоимости товара
# amount = int(input("Введите стоимость товара: "))
#
# # Перебираем монеты от самой большой к самой маленькой
# for coin in coins:
#     count = amount // coin  # сколько монет этого номинала нужно
#     if count > 0:
#         print("Внесите монеты номиналом", coin, ":", count)
#         amount %= coin  # уменьшаем сумму на использованные монеты

# ======igive kodebia magram daakvirdi kargad =======
# coins = [50, 10, 5, 2, 1]
# amount = int(input("Введите стоимость товара: "))
#
# for coin in coins:
#     count = amount // coin
#     if count > 0:
#         print("Внесите монеты номиналом", coin, ":", count)
#         amount %= coin








