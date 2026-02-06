#
# nun1 = {')': '(', ']': '[', '}': '{'}
#
# tests = ["({[}])", "([({}()){}])"]
#
# for nun2 in tests:
#     num = []
#     rom = True
#     for n in nun2:
#         if n in "([{":
#             num.append(n)
#         elif n in ")]}":
#             if not num or num.pop() != nun1[n]:
#                 rom = False
#                 break
#     if num:
#         rom = False
#
#     print(f"Скобки: {nun2}\nВалидны: {rom}\n")

# nun = [5, 3, 4, 2, 1, 5, 3]
# num = []
#
# for n in nun:
#     if n == 5:
#         num.append([n, "отлично"])
#     elif n in (3, 4):
#         num.append([n, "хорошо"])
#     else:
#         num.append([n, "неудовлетворительно"])
#
# print(num)

# set1 = {1, 2, 3, 4}
# set2 = {2, 5}
# print(set2.issubset(set1))
#
# set1 = {1, 2, 3, 4,}
# set2 = {2, 3}
# print(set2 <= set1)

# set1 = {1, 2, 3, 4}
# set2 = {2, 5}
#
# is_subset = True
# for element in set2:
#     if element not in set1:
#         is_subset = False
#         break
#
# print(is_subset)  # True


#
# string = input("Введите строку со скобками: ")
#
# stack = []
# pairs = {')': '(', ']': '[', '}': '{'}
# valid = True
#
# for ch in string:
#     if ch in pairs.values():
#         stack.append(ch)
#     elif ch in pairs:
#         if not stack or stack[-1] != pairs[ch]:
#             valid = False
#             break
#         stack.pop()
#     else:
#         # Игнорируем символы, не являющиеся скобками
#         continue
#
# if stack:
#     valid = False
#
# print(f"\nСкобки: {string}")
# print(f"Валидны: {valid}")
#

































