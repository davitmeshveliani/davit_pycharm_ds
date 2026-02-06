#(metodi rit gansxvavdeba funkciisgan?)
#()funqciiis
#(mtodi) miekutvneba konkretul obieqts tips . წერ-ილს გამოიძახება ობიექტი

 # Форматирование строки и целого числа
# name = "Alice"
# age = 30
# print("My name is " + name + " and I am " + str(age) + " years old.")
# text = "My name is %s and I am %d years old." % (name, age)
# # text = "My name is %s and I am %d years old." % (age, name)
# print(text)
# print("My name is %s and {} I am %d years old." % (name, age))
#
# # Форматирование числа с плавающей точкой
# pi = 3.14159
# text = "The value of pi is approximately %.3f." % pi
# print(text)

# name = "Alice"
# age = 30
# text = "My name is {} and I am {} years old."
# # print(text.format(name, age))
# print(text.format(input("Enter name: "), input("Enter age: ")))
# print("My name is Alice and I am 30 years old.")
# print(text.format("Bob", 36))
# print(text.format("name", 34))
#
# name1 = "Alice"
# age1 = 30
# text = "My name is {name} and I am {age} years old. Are you also {age} years old?"
# # print(text.format(age=25, name="Bob"))
# print(text.format(age=age1, name=name1))
# # print(age)
# text = "Her name is {0} and she is {1} years old. {0} loves Python."
# print(text.format("Anna", 28))

# text = "The {1} and {0} is {color}."
# print(text.format("sky", "sea", color="blue"))

# # name = "Alice"
# # age = 25
# name = input("Enter name: ")
# age = input("Enter age: ")
# # text = f"My name is {name} and I am {age} years old."
# # print(text)
# print(f"My name is {name} and I am {age} years old.")
# # print(f"My name is {input()} and I am {input()} years old.")

#
# x = 10
# y = 20
# text = f"The sum of {x} and {y} is {x + y} {input().upper()}."
# print(text)
#
# name = "Charlie"
# age = 30
# text = f"""Info
# Name: {name}
# Age: {age}
# """
# print(text)
#

# pi = 3.14159
# f-строки
# :.2f
# text_fstring = f"Pi rounded to 2 decimal places is {pi:.2f}"
# text_fstring2 = f"Pi rounded to 2 decimal places is {3.14159:.2f}"
# # Метод format()
# text_format1 = "Pi rounded to 2 decimal places is {:.2f}".format(pi)
# text_format2 = "Pi rounded to 2 decimal places is {0:.2f}".format(pi)
# text_format3 = "Pi rounded to 2 decimal places is {num:.2f}".format(num=pi)
# print(text_fstring)
# print(text_fstring2)
# print(text_format1)
# print(text_format2)
# print(text_format3)

# large_number = 1234567890
# # f-строки
# text_fstring = f"The number with thousand separators: {large_number:,}"
# # Метод format()
# text_format = "The number with thousand separators: {:,}".format(large_number)
# print(text_fstring)
# print(text_format)


# # f-строки
# text_fstring = f"start_{'text':>10}_end"
# # Метод format()
# # text_format = "start_{:>10}_end"
# # text_format = "start_{:<10}_end"
# text_format = "start_{:^10}_end"
# print(text_fstring)
# print(text_format.format("text"))


# number = 40
# text = 'hi'
# # f-строки
# text_fstring = f"start_{number:5}_end"
# # Метод format()
# text_format = "start_{:5}_end"
# print(text_fstring)
# print(text_format.format(text))

#
# # Заполнение нулями
# number = 40
# text = f"{number:0>5}"
# print(text)
#
# # Заполнение нижним подчеркиванием
# # text = f"{'Python':^10}"
# text = f"{'Python':_^10}"
# text = f"{'PythonPython':_^10}"
# print(text)
#
#
# text = "Python"
#
# # ljust(): выравнивание по левому краю
# print(text.ljust(15))
# print(text.ljust(15, '-'))
# # rjust(): выравнивание по правому краю
# print(text.rjust(15))
# print(text.rjust(15, '-'))
# # center(): выравнивание по центру
# print(text.center(15))
# print(text.center(15, '-'))

# number = 1234.5678
# print(f"Formatted number: {number:.2f}")

# Напишите программу, которая принимает дату в виде числа, месяца и года,
# а затем выводит её в формате "dd/mm/yyyy", где день и месяц всегда состоят из двух цифр.
#
# Пример вывода:
#
# Введите день: 3
# Введите месяц: 7
# Введите год: 2024
# Дата: 03/07/2024

# day = "3"
# month = "7"
# year = "2024"
# print(f"Дата: {day:0>2}/{month:0>2}/{year}")



