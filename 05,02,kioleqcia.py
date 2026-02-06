## 1 #############

# n = int(input("Введите число: "))

# for i in range(1, n + 1):
#     for nun in range(1, n + 1):
#         print(i * nun, end="\t")
#     print()

###  2 ########

# n = int(input("Введите число: "))
#
# for i in range(1, n + 1):
#     for nun in range(1, i + 1):
#         print(nun, end=" ")
#     print()

###   3 ######

# text = input("Введите строку: ")
# result = ""
#
# for char in text:
#     if char not in result:
#         result += char
#
# print("Результат:", result,end=" ")


# price = int(input("Введите стоимость товара: "))
#
# coins = list([50, 10, 5, 2, 1])
#
# for c in coins:
#     if price >= c:
#         k = price // c
#         print("Внесите монеты номиналом", c, ":", k)
#         price = price % c
#


# numbers = [4, 9, 1, 7, 2, 5, 0, 3, 7, 1, 3]
#
# print("Изначальный список:", numbers)
#
# for i in range(len(numbers)):
#     if numbers[i] % 2 != 0:
#         numbers[i] = numbers[i] ** 2
#
# print("Измененный список: ", numbers)

###########################################
# numbers = [4, 9, 1, 7, 2, 5, 0, 3, 7, 1, 3]
#
# print("Изначальный список:", numbers)
#
# i = 0
# while i < len(numbers):
#     if numbers[i] % 2 == 1:
#         numbers[i] = numbers[i] * numbers[i]
#     i += 1
#
# print("Измененный список: ", numbers)









