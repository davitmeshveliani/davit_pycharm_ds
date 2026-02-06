# д.э- №-1
#
# nun = [5, 3, 4, 2, 1, 5, 3]
#
# num = [[n, "отлично"] if n == 5 else [n, "хорошо"] if n in (3, 4) else [n, "неудовлетворительно"] for n in nun]
#
# print(num)

##################################


# д.э- №-2

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
#
