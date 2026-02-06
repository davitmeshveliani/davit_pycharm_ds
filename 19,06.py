#
# numbers = [5, 2, 3, 8, 4, 1, 2, 7]
#
# nun = []  # აქ შევინახავთ (ინდექსი, მნიშვნელობა) ყველა წყვილი რიცხვს
#
#
#
# i = 0
# while i < len(numbers):
#     if numbers[i] % 2 == 0:
#         nun.append((i, numbers[i]))
#     i += 1
#
# values_sorted = []
# i = 0
# while i < len(nun):
#     values_sorted.append(nun[i][1])
#     i += 1
#
# values_sorted.sort(reverse=True)
#
# i = 0
# while i < len(nun):
#     index = nun[i][0]
#     numbers[index] = values_sorted[i]
#     i += 1
# #
# # print("Список после сортировки:", numbers)
#
# #
#
# numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
# nun = int(input("Введите число для удаления кратных ему элементов: "))
# i = 0
#
# while i < len(numbers):
#     if numbers[i] % nun == 0:
#         numbers.pop(i)
#     else:
#         i += 1
#
# print("Список без кратных значений:", numbers)
#
# #
# text = "Programming in python"
# print("Строка:", text)
#
# text = text.lower()
# nun = ""
#
# i = 0
# while i < len(text):
#     char = text[i]
#     if char not in nun:
#         count = text.count(char)
#         if count > 1:
#             print(f"Символ '{char}' встречается {count} раз(а)")
#         nun += char
#     i += 1


# strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
# result = []
#
# for s in strings:
#     i = 0
#     # ვეძებთ პირველ ციფრს სტრიქონში
#     while i < len(s) and not ('0' <= s[i] <= '9'):
#         i += 1
#
#     # შემოწმება, დარჩენილ სიმბოლოებს შორის არის თუ არა არ ციფრი
#     for nun in s[i:]:
#         if nun < '0' or nun > '9':
#             break
#     else:
#         result.append(s)
#
# print("Строки с цифрами только в конце:", result)
#




















