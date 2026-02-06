#
# Напишите программу, которая обрабатывает список из строк и удаляет все строки, содержащие более одного слова,
# а также преобразует оставшиеся строки к нижнему регистру.
#
# Данные:
#
# text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
#
# Пример вывода:
#
# Обработанный список: ['hello', 'world', 'simple']
#
# text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
#
# result = []
#
# for text in text_list:
#     if len(text.split()) == 1:
#         result.append(text.lower())
#
# print(result)


# products = [
#     ["Laptop", 1200],
#     ["Mouse", 25],
#     ["Keyboard", 75],
#     ["Monitor", 200],
#
# ]
#
# nun = float(input("Введите скидку (в процентах): "))
# for product in products:
#     old_price = product[1]
#     new_price = round(old_price * (100 - nun) / 100, 2)
#     product.append(new_price)
#
# print("\nТовар           Старая цена      Новая цена\n")
# for item in products:
#     name = item[0]
#     old = f"{item[1]:>12.2f}$"
#     new = f"{item[2]:>13.2f}$"
#     print(f"{name:<15}{old}{new}")

#
# text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
#
# for text in text_list:
#     if " " not in text:
#         print(.lower())

