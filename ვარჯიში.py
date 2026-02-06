# # # 1. სია ცხოველებით
# # nun_list = ["cat", "dog", "elephant"]
# #
# # # 2. ციკლი enumerate-ით, ინდექსი 1-დან
# # for i, animal in enumerate(nun_list, 1):
# #     print(f"{i}. {animal}")
#
# #
# # # 3. ტიუპლი რიცხვებით
# # numbers = (10, 20, 20, 30, 10, 40)
# #
# # # 4. რამდენჯერ არის 20
# # count_20 = numbers.count(20)
# # print(f"რიცხვი 20 არის {count_20} ჯერ")
# #
# # first_10_index = numbers.index(10)
# # print(f"პირველი 10 არის პოზიციაზე: {first_10_index}")
#
# # numbers = (10, 20, 20, 30, 10, 40)
# #
# # # პირველი 10-ის ინდექსი (0-დან)
# # index_0 = numbers.index(10)
# #
# # # ადამიანები 1-დან იწყებენ მთვლას, ამიტომ დავამატოთ 1
# # position = index_0 + 1
# #
# # print(f"ელემენტი 10 დგას ნომერზე: {position}")
# #
#
#
# # import datetime
# #
# # def main():
# #     now = datetime.datetime.now()
# #     print(f"სკრიპტი შესრულდა: {now}")
# #
# #     with open("log.txt", "a", encoding="utf-8") as f:
# #         f.write(f"სკრიპტი შესრულდა: {now}\n")
# #
# # if __name__ == "__main__":
# #     main()
# #
#
# #
# # text = "hello world"
# # unique_chars = list(set(text.replace(" ", "")))
# #
# # print("Уникальные символы:", unique_chars)
#
# # /////////////////////////////////
# # text = "hello world"
# #
# # unique_chars = []
# # for char in text:
# #     if char != " " and char not in unique_chars:
# #         unique_chars.append(char)
# #
# # print("Уникальные символы:", unique_chars)
#
#
#
# # nun = int(input("Введите конец диапазона: "))
# #
# # nun1 = [i**2 for i in range(1, nun + 1) if i % 2 == 0]
# #
# # print(nun1)
# #
# # ###№########
# # nun = int(input("Введите конец диапазона: "))
# #
# # for i in range(2, nun + 1, 2):  # шаг 2 — только чётные
# #     print(f"{i}^2 = {i**2}")
#
#
# #
# wörter = ["apple", "cherry", "kiwi", "banana", "orange"]
# print(wörter)
# zeichen = input("Исключить символ: ")
# andere_wörter = [word for word in wörter if zeichen not in word]
# print(andere_wörter)
#
# text = "Apple orange apple banana Orange"
# words = text.lower().split()
# unique_words = set(words)
#
# print("Уникальные слова:", unique_words)
# print("Количество уникальных:", len(unique_words))

#
# # : "золото, серебро, рубины, алмазы"
# nun1_input = input("Введите сокровища первого сундука (через запятую): ")
# chest2_input = input("Введите сокровища второго сундука (через запятую): ")
#
# nun1 = set(item.strip() for item in nun1_input.split(","))
# nun2 = set(item.strip() for item in chest2_input.split(","))
#
# only_in_first = nun1 - nun2
# common = nun1 & nun2
# all_unique = nun1 | nun2

# print("Только в первом сундуке:", only_in_first)
# print("Общее в обоих сундуках:", common)
# print("Все уникальные драгоценности:", all_unique)



# set1 = {1, 2, 3, 4}
# set2 = {2, 3}
# print(set2.issubset(set1))

# set1 = {1, 2, 3, 4}
# set2 = {2, 3}
# print(set2 <= set1)



# set1 = {2, 3, 4, 5, 6,7,8,9}
# set2 = {4, 5}
#
# if set2.issubset(set1):
#     print("Подмножество: True")
#     print("Разница:", set1 - set2)
# elif set1.issubset(set2):
#     print("Подмножество: True")
#     print("Разница:", set2 - set1)
# else:
#     print("Подмножество: False")
