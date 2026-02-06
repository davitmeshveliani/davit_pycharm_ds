# a = 5
# b = 25
# print(a + b < 0 and b < 0 or a != 5)
# print(15 > 0 and 10 > 0 or 5 != 5)
# print(True and False or True)
# #print(True)

# a = int(input("Введите первое число"))
# b = int(input("Введите второе число"))
# print(a*b,a,b,sep="_")

# a = 5
# b = 10
# print(a + b > 0 and b > 0 or a == 5)
# print(15 > 0 and 10 > 0 or 5 == 5)
# # print(True and True or True)
# # print(True or True)
# # print(True)

#############################################

######
# Ввод значений от пользователя
# light_input = input("Свет включён? (True/False): ")
# door_input = input("Дверь открыта? (True/False): ")
#
# light = light_input == "True"
# door = door_input == "True"
#
# if light and door:
#     result = "Оба условия выполнены"
# elif light or door:
#     result = "Хотя бы одно условие выполнено"
# else:
#     result = "Ни одно из условий не выполнено"
#
# # Вывод результатов
# print("Свет включён?", light)
# print("Дверь открыта?", door)
# print(result)

###################################################
# Напишите программу, которая получает два числа от пользователя и вычисляет:
#
# Остаток от деления
#
# Результат целочисленного деления
#
# Решить без использования операторов % и //.


# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
#
# c = int(a / b)
# result = a - (b * c)
#
# print("Остаток от деления:", result)
# print("Целочисленное деление:", c)


# # Получаем числа от пользователя
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
#
# # Выводим результат умножения и сами числа через дефис
# print("Результат:", a * b, a, b, sep='-')
