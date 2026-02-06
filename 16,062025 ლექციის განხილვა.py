# my_tuple = (1, 2, 3, "apple", True)
# print(my_tuple)
#
# print(1, 2, 3, "apple", True)
# print((1, 2, 3, "apple", True))
#
# empty_tuple = ()
# print(empty_tuple) # Вывод: ()

# single_element_tuple = (5)
# single_element_tuple = (True,)
# single_element_tuple = ([2, 3, 4],)
# print(single_element_tuple)
# print(type(single_element_tuple))

# my_tuple = (10, 20, 30, 40)
# print(my_tuple[1])
# print(my_tuple[-1])

# my_tuple = (10, 20, 30)
# # Попытка изменить элемент вызовет ошибку
# my_tuple[1] = 40
# print(my_tuple)
# # TypeError: 'tuple' object does not
# # support item assignment

# tuple1 = (1, 2)
# tuple2 = (3, 4)
# print(tuple1 + tuple2) # Конкатенация кортежей
# my_tuple = (1, 2)
# print(my_tuple * 3) # Повторение кортежей
# my_tuple = (10, 20, 30)
# print(20 in my_tuple) # Проверка на наличие элемента
# # in_tuple = False
# # for el in my_tuple:
# #     if el == 20:
# #         in_tuple = True
# # print(my_tuple)
#
# my_tuple = (1, 2, 3, 4, 5)
# print(len(my_tuple)) # Длина кортежа
# # Сравнение кортежей происходит аналогично спискам, то есть поэлементно
# tuple1 = (1, 2, 3)
# tuple2 = (1, 2, 4)
# print(tuple1 == tuple2) # Сравнение кортежей

# my_tuple = (1, 2, 3)
# my_list = list(my_tuple)
# print(my_list)
# print(type(my_list))

# print(tuple([5]))

# my_tuple = (10, 20, 30, 40)
# for item in my_tuple:
#     print(item)

# a = 4
# packed_tuple = 1, 2, 3, a, a + 10
# # packed_tuple, packed_tuple2 = 1, 2, 3, a, a + 10
# print(packed_tuple)
# print(type(packed_tuple))

# # Кортеж с тремя элементами
# packed_tuple = (1, 2, 3)
# # Распаковка значений кортежа в переменные
# a, b, c = packed_tuple
# # a, b = packed_tuple
# print(a, b, c)
# print(b)
# print(len(packed_tuple))
# # print(len(a, b, c))

# numbers = [1, 2, 3, 4, 5]
# # Вывод коллекции
# print(numbers)
# print(numbers[0], numbers[1], numbers[2], numbers[3], numbers[4], sep="-")
# # Вывод элементов по отдельности
# print(*numbers, sep="-")
# print(*[1, 2, 3, 4, 5], sep="-")
# print(*(1, 2, 3, 4, 5), sep="-")

# numbers = [1, 2, 3, 4, 5]
# # Распаковка первого элемента в a,
# # последнего в b, остальные элементы в other
# a, *other, b = numbers
# print(a)
# print(b)
# print(other)
#
# a, b, *other = numbers
# print(a)
# print(b)
# print(other)


# pairs = [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
# for pair in pairs:
# # Распаковка элементов кортежа в переменные
#     print(pair)
#     print(f"Число: {pair[0]}, Фрукт: {pair[1]}")
#
# for number, fruit in pairs:
# # Распаковка элементов кортежа в переменные
#     print(f"Число: {number}, Фрукт: {fruit}")
#
# pairs = [(1, 'apple', "eser"), (2, 'banana', 2, 6), (3, 'cherry')]
# for number, fruit, *_ in pairs:
# # Распаковка элементов кортежа в переменные
#     print(f"Число: {number}, Фрукт: {fruit}")


# fruits = ["apple", "banana", "cherry"]
# enumerated_fruits = enumerate(fruits)
# Чтобы увидеть содержимое, преобразуем
# объект enumerate в список
# print(enumerated_fruits)
# print(list(enumerated_fruits))
# for t in enumerate(fruits):
#     print(t)
#
# for i, fruit in enumerate(fruits):
#     print(i, fruit)
#     if not i % 2:
#         fruits[i] = fruit.upper()
# print(fruits)

# for t in enumerate("fruits"):
#     print(t)
#
# for t in enumerate("fruits", 1):
#     print(t)
#
# numbers = [10, 20, 15, 30, 25, 35]
# for index, value in enumerate(numbers[:-1]): # Проходим по списку, кроме последнего элемента
#     if value > numbers[index + 1]:
#         print(f"{value} больше, чем {numbers[index + 1]}")

# fruits = ["apple", "banana", "cherry"]
# for index, fruit in enumerate(fruits):
#     print(f"{index}: {fruit}", end=' ')

# my_tuple = (1, 2, 3, 2, 4, 2)
# count_of_twos = my_tuple.count(2)
# print(count_of_twos)

# my_tuple = (10, 20, 30, 20, 40)
# index_of_first_twenty = my_tuple.index(20)
# print(index_of_first_twenty)
# index_of_twenty_in_range = my_tuple.index(20, 2) # Начинаем поиск с индекса 2
# print(index_of_twenty_in_range)

# my_tuple = (10, 20, 30, 20, 40)
# my_tuple[1] = 200

# my_tuple = (10, [20, 30], 20, 40)
# my_tuple[1][0] = 0
# # # my_tuple[1] = 200
# # l = my_tuple[1]
# # print(l)
# # l[0] = 200
# # print(l)
# print(my_tuple)
