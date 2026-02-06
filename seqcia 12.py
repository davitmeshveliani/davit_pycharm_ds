# Напишите программу, которая обрабатывает список float чисел,
# вычисляет сумму положительных чисел.
# Результат необходимо вывести в формате денежной суммы
# (до 2 символов после запятой),
# добавляя символ валюты "$" вначале
# и разделяя тысячи запятой.
#
# Данные:
#
# numbers = [1245.4435, -302.1403, 87459.99, -520.8265, 1450.001]
#
#
# Пример вывода:
#Сумма положительных чисел: $90,155.43
#
#
# numbers = [1245.4435, -302.1403, 87459.99, -520.8265, 1450.001]
#
# total_positive = sum(num for num in numbers if num > 0)
# formatted_total = f"${total_positive:,.2f}"
#
# print(f"Сумма положительных чисел: {formatted_total}")
#########----------------------------------

# data_list = [
#     "John 23 12345.678",
#     "Alice 30 200.50",
#     "Bob 35 15000.3",
#     "Charlie 40 500.75"
# ]
#
# print(f"{'Имя':<10} {'Возраст':>3} {'Баланс':>10}")
# for entry in data_list:
#     name, age_str, balance_str = entry.split()
#     age = int(age_str)
#     balance = float(balance_str)
#     print(f"{name:<10} {age:>3} {balance:>10.2f}")

#----------------------13,06,2025 dvalebis ganxilvaa

# text = "Programming in python"
# text = text.lower()
#
# for char in set(text):
#     count = text.count(char)
#     if count > 1:
#         print(f"Символ '{char}' встречается {count} раз(а)")
#


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























