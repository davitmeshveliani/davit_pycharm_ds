# Звёздочки вместо чисел
# Напишите программу, которая заменяет все цифры
# в строке на звёздочки *.
#
# text = "My number is 123-456-789"
# Пример вывода:
#
# Строка: My number is 123-456-789
# Результат: My number is ***-***-***

# Замена цифр на * одной строкой
#\\\\\\\\\ 1,1 \\\\\\\\

text = "My number is 123-456-789"
result = "".join("*" if ch.isdigit() else ch for ch in text)
print(result)
#\\\\\\\\\\\\  1,2 \\\\\\\\\\\\\

text = "My number is 123-456-789"
result = ""
for ch in text:
    if ch.isdigit():
        result += "*"
    elif ch == "-":
        result += "-"
    else:
        result += ch
print("Строка:", text)
print("Результат:", result)

################################\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Количество символов
#
# Напишите программу, которая подсчитывает количество вхождений всех символов в строке.
# Нужно вывести только символы, которые встречаются более 1 раза (игнорируя регистр),
# с указанием их количества.
# Выводите повторяющиеся символы только один раз.
#
# text = "Programming in python"
#
# Пример вывода:
# Строка: Programming in python
# Символ 'p' встречается 2 раз(а)
# Символ 'r' встречается 2 раз(а)
# Символ 'o' встречается 2 раз(а)
# Символ 'g' встречается 2 раз(а)
# Символ 'm' встречается 2 раз(а)
# Символ 'i' встречается 2 раз(а)
# Символ 'n' встречается 3 раз(а)
# Символ ' ' встречается 2 раз(а)

# from collections import Counter
# text = "Programming in python"
# text_lower = text.lower()
# char_count = Counter(text_lower)
# print("Строка:", text)
# for ch, count in char_count.items():
#     if count > 1:
#         print("Символ", "'" + ch + "'", "встречается", count, "раз(а)")


#############################################\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Увеличение чисел
# Напишите программу, которая заменяет все числа в строке на их эквивалент, умноженный на 10.
# text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
# Пример вывода:
# I have 50.0 apples and 100.0 oranges, price is 5.0 each. Card number is ....3672.

# text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
#
# words = text.split()
# new_words = []
#
# for word in words:
#     if word.isdigit():
#         new_words.append(str(int(word) * 10))
#     else:
#         new_words.append(word)
#
# result = " ".join(new_words)
# print(result)
