
# def explain_dictionary():
#     """
#     ფუნქცია ახსნის Python-ის ლექსიკონს (dictionary) მოკლედ, მაგალითებით და გამოყენებით.
#     """
#
#     explanation = """
#     ლექსიკონი (dictionary) — მონაცემთა სტრუქტურა, რომელიც შენახავს წყვილებს: გასაღები (key) და მნიშვნელობა (value).
#
#     - გასაღებები უნიკალური უნდა იყოს და ზოგადად, სტრინგი, რიცხვი ან tuple შეიძლება იყოს.
#     - მნიშვნელობა შეიძლება იყოს ნებისმიერი ტიპის მონაცემი.
#
#     მაგალითი ლექსიკონის შექმნისა:
#         person = {"სახელი": "დატო", "ასაკი": 25}
#
#     მნიშვნელობების წვდომა:
#         print(person["სახელი"])  # შედეგი: დატო
#
#     ახალი ელემენტის დამატება:
#         person["ქალაქი"] = "თბილისი"
#
#     ლექსიკონის ელემენტების გავლა:
#         for key, value in person.items():
#             print(key, value)
#
#     გასაღების არსებობის შემოწმება:
#         if "ასაკი" in person:
#             print("ასაკი არსებობს")
#     """
#
#     print(explanation)
#
#
# if __name__ == "__main__":
#     explain_dictionary()
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for num in numbers:
#     if num % 2 == 0:
#         print(num, "არის ლუწი")
#     else:
#         print(num, "არის კენტი")
#---------------------------------------------------------
# numbers = [3, 8, 12, 5, 7, 10, 1, 6, 9, 2]
#
# even_count = 0
# odd_count = 0
#
#
# for number in numbers:
#     if number % 2 == 0:
#         print(f"{number} არის ლუწი")
#         even_count += 1
#     else:
#         print(f"{number} არის კენტი")
#         odd_count += 1
#
# print("ლუწი რიცხვების რაოდენობაა:", even_count)
# print("კენტი რიცხვების რაოდენობაა:", odd_count)

# -------------------------------------------- # იტერაცია

# text = "My number is 123-456-789"
# result = ""
#
# for char in text:
#     if char.isdigit():
#         result += "*"
#     else:
#         result += char
#
# print("Строка:", text)
# print("Результат:", result)

##################################################################################
# import re
# text = "My number is 123-456-789"
# result = re.sub(r"\d", "*", text)
#
# print("Строка:", text)
# print("Результат:", result)
##################################################################
#
# text = "My number is 123-456-789"
#
# result = ''.join(['*' if char.isdigit() else char for char in text])
#
# print("Строка:", text)
# print("Результат:", result)
# result = ''.join(['*' if char.isdigit() else char for char in text])
#
# print("Строка:", text)
# print("Результат:", result)
##########################################################################
# text = "My number is 123-456-789"
#
# trans = str.maketrans("0123456789", "**********")
#
# result = text.translate(trans)
#
# print("Строка:", text)
# print("Результат:", result)
#######################################################################

########################################
# from collections import Counter
#
# text = "Programming in python"
# text_lower = text.lower()
#
# char_counts = Counter(text_lower)
#
# print("Строка:", text)
#
# for char, count in char_counts.items():
#     if count > 1:
#         print("Символ", repr(char), "встречается", count, "раз(а)")
# Сложение чисел
# Напишите программу, которая принимает строку с числами через пробел и выводит сумму всех чисел.
#-------------------------------------------------
# # Пример вывода:
# # Введите список чисел через пробел: 1 2 3 4 5
# # Сумма чисел: 15
#
# a = input("Введите список чисел через пробел:")
# nums = a.split()
# print(nums)
# resals = 0
# for num in nums:
#
#     resals += int(num)
# print(resals)

#################     11,06,2025,  vrjishi

#
# Пример вывода:
# Изначальный список: [-1, 8, 2, 0, -3, -9, -1, 10, 7, -4]
# Сумма чётных: 16
# Сумма нечётных: -7

# numbers = [-1, 8, 2, 0, -3, -9, -1, 10, 7, -4]
#
# sum_1 = 0
# sum_2 = 0
#
# for x in numbers:
#     if x % 2 == 0:
#         sum_2 += x
#     else:
#         sum_1 += x
# print(sum_1, sum_2)

# Максимальное число
# Напишите программу, которая выводит наибольшее число в списке,
# не используя встроенную функцию max(), а также его индекс в списке.
# numbers = [3, 12, 8, 22, 9, 25, 6, 23, 8, 7]

# numbers = [3, 12, 8, 22, 9, 25, 6, 23, 8, 7]
#
# max_num = numbers[0]
# index = 0
#
# for i in range(1, len(numbers)):
#     if numbers[i] > max_num:
#         max_num = numbers[i]
#         index = i
#
# print(max_num)
# print(index)
######---------------------------------------
# Числа и слова
# Напишите программу, которая обрабатывает строку, содержащую слова
# и целые числа, разделённые пробелами. Программа должна преобразовать
# строку в список, где числа преобразуются в тип int,
# а остальные элементы остаются строками и начинаются с заглавной буквы.
# text = "apple 42 banana 3 100 orange"
#
# Пример вывода:
# Изначальная строка: apple 42 banana 3 100 orange
# Результат: ['Apple', 42, 'Banana', 3, 100, 'Orange']

# text = "apple 42 banana 3 100 orange"
# words = text.split()
# print(words)
# print(type(words))
# print(words[1].isdigit())
# for i in range(len(words)):
#     if words[i].isdigit():
#         words[i] = int(words[i])
#     else:
#         words[i] = words[i].capitalize()
# print(words)


# Проверка формата email
# Напишите программу, которая проверяет, начинается ли строка
# с буквы, содержит ли в себе символ @, и заканчивается ли на .com или .de.
#
# Пример вывода:
# Введите email: user@example.com
# Корректный формат? Tru

# name = input("Введите email:")
#
# if name[0].isalpha() \
#     and "@" in name \
#     and (name.endswith(".com") or name.endswith(".de")):
#     print(True)
#
# Напишите программу, которая подсчитывает количество вхождений всех символов в строке. Нужно вывести только символы, которые встречаются более 1 раза (игнорируя регистр), с указанием их количества. Выводите повторяющиеся символы только один раз.

# text = "Programming in python"
#
# Пример вывода:
#
# Строка: Programming in python
#
# Символ 'p' встречается 2 раз(а)
#
# Символ 'r' встречается 2 раз(а)
#
# Символ 'o' встречается 2 раз(а)
#
# Символ 'g' встречается 2 раз(а)
#
# Символ 'm' встречается 2 раз(а)
#
# Символ 'i' встречается 2 раз(а)
#
# Символ 'n' встречается 3 раз(а)
#
# Символ ' ' встречается 2 раз(а)




# text = "Programming in python"
# print("Строка:", text)
# text = text.lower()
# counted = []
# for char in text:
#     if text.count(char) > 1 and char not in counted:
#         print("Символ", "'", char, "'", "встречается", text.count(char), "раз(а)")
#         counted.append(char)



# text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
# words = text.split()
# for i in range(len(words)):
#     if words[i].replace('.', '', 1).isdigit():
#         words[i] = str(float(words[i]) * 10)
# result = " ".join(words)
# print(result)










