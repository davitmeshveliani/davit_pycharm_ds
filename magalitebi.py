

############## pithoni 15#####
# s = "Hello"
# print(s + " world!")
# print(s)
# s = "new"
# print(s)

# s = "Python"
# s += " is fun"
# s = 5
# # s = s + " is fun"
# d = s
# print(s)
#


# text = "hello"
# print(text.encode('utf-8'))
# # Кодирует текст, полученный из
# # переменной text в 'utf-8'


#
# text = "Python"
# # Метод .encode() кодирует строку в байты с использованием UTF-8
# encoded_text = text.encode('utf-8')
# print(encoded_text)

# # Оригинальная строка
# text = "Привет"
#
# # Кодирование строки в байты с использованием UTF-8
# encoded_text = text.encode('utf-8')
# print(encoded_text)
#
# # Декодирование байтов обратно в строку
# decoded_text = encoded_text.decode('utf-8')
# print(decoded_text)


# print(ord('A'))
# print(ord('a'))
# print(ord(' '))
# print(chr(65))
# print(chr(97))
# print(chr(108))

# print("apple" == "apple")
# print("apple" == "banana")
# print("apple" == "Apple")
# print("apple" == "applE")
# print("apple" != "ap ple")
#
# print(ord("a"))
# print(ord("b"))
# print("appledgfdfgdf" < "banana")
# # True('a' < 'b')
# print("Cpple" < "banana")
# # True ('A' < 'b')
# print("apple" > "Apple")
# # True ('a' > 'A')

# print("appleqqqqqqqqqqqqqqqq" < "application")
# print("apple" < "app")
# print("a" < "DGDGFGSFGYJTKTEYK")

# text = " Python   "
# length = len(text)
# print(length)
# print(len("Python") < len("Pyt"))
#
# text = "Python"
# # print(text[0])   # Вывод: 'P' (первый символ)
# # print(text[2])   # Вывод: 't' (третий символ)
# # # print(input(">")[0])
# # print("fdgdf"[1])
# print(text[-1])
# print(text[-2])

# text = "hello"
# # print(text[67])
# print(text[-6])  # Ошибка, так как в строке "hello" всего 5 символов

# text = "hello"
# index = 3
# if index < len(text):
#     print(text[index])
# else:
#     print("Индекс вне диапазона!")

# text = "Python programming"
# print(text[1:3])
# print(text[1,3])

# text = "Python programming"
# print(text[:3])
# print(text[7:])
# print(text[:])
#
# good_num = "N:345253"
# good2_num = "N:556767"
# print(good_num[2:])
# print(good2_num[2:])

# text = "Python programming"
# print(text[-11:])

# text = "Python programming"
# print(text[-11:-4])  # -11 < -4
# print(text[7:14])  # 7 < 14
#
# text = "Python programming"
# print(text[-4:-11])  # Пустая строка
# print(text[14:7])  # Пустая строка

# text = "Hello, Python!"
# print(text[1:6])

# text = "Python programming"
# # print(text[234])
# print(text[0:234])
# print(text[6:0])

# text = "Python programming"
# print(text[-11:])
# print(text[-11:-15])
# print(text[-15:-10])

# Положительный шаг
# text = "Python programming"
# print(text[0:12:2])  # Вывод: 'Pto rg'
# print(text[1:12:3])  # Вывод: 'Pto rg'

# # # Отрицательный шаг (обратный порядок)
# text = "Python programming"
# print(text[12:6:-1])
#print(text[6:12:-1])

# text = "Python"
# print(text[::-1])  # Вывод: 'nohtyP'
#
# text = "Python programming"
# print("t" in text)
# print("a" in text)
# print("Python" in text)
# print("pro" in text)
# print("Hello" in text)

# text = "Python programming"
# print("Java" not in text)

# text = "Python programming"
# print("python" in text)
# print("o" in text)
###--------------------------------------------------

#------ეს არის სოცჰიკის  ცტილი
# ამას ეწოდება ციკლის შეწყვეტა (break) და ის გამოიყენება
# while ან for ციკლში, როდესაც გინდა, რომ ციკლი დასრულდეს
# ნაადრევად გარკვეული პირობის შესრულებისას.

#
# g = int(input("შეიყვანე რიცხვი: "))
# a = 0
#
# if g >= 0:
#     while a <= g:
#         print(a)
#         a += 1
# else:
#     print("შეიყვანე ნულის ტოლი ან მეტი რიცხვი.")

# g = int(input("შეიყვანე რიცხვი: "))
# a = 0
#
# if g >= 0:
#     while a <= g:
#         if a == 5:
#             break  # ციკლი შეწყდება როცა a გახდება 5
#         print(a)
#         a += 1
# else:
#     print("შეიყვანე ნულის ტოლი ან მეტი რიცხვი.")
#-------------------------------------------------------

# i = 1
# while i <= 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1

# g = int(input("Digite un numero: "))
# a=0
# if g >= 10:
#     while a<=g:
#         if a == 5:
#             break
#         print(a)
#         a +=1
# else:
#     #
#     # print("a =0", "a >0", )
#     print(g)
#---------------------------
#% — ნაშთის ოპერატორი
# a % b ნიშნავს გაყო a რიცხვი b-ზე და აიღე ნაშთი.
#
# მაგალითად:
#
# 5 % 2 → 2 ორჯერ მოთავსდება 5-ში, დარჩება ნაშთი 1
#
# 4 % 2 → 2 ორჯერ მოთავსდება 4-ში, ნაშთი 0


# i = 1
# while i <= 10:
#     if i % 2 != 0:  # თუ რიცხვი კენტია
#         print(i)
#     i += 1
##########
# i = 10
# if i % 2 != 0:
#     print("კენტია")
# else:
#     print("ლუწია")

#✅ სავარჯიშო 5: შეიყვანე რიცხვები მანამ, სანამ "0"-ს არ შეიყვანს
# while True:
#     num = int(input("შეიყვანე რიცხვი (გასაჩერებლად შეიყვანე 0): "))
#     if num == 0:
#         print("შეყვანა შეწყდა.")
#         break
#     print("შეიყვანე:", num)
#----------------------------------
# აი ✅ სავარჯიშო 1-ის გადაწყვეტა:
# შეიყვანე რიცხვები მანამ, სანამ 0-ს არ შეიყვან, და დაბეჭდე მათი ჯამი

# სავარჯიშო 1: შეყვანილი რიცხვების ჯამი 0-მდე

# total = 0
#
# while True:
#     num = int(input("შეიყვანე რიცხვი (0-ს შეყვანა დასრულებს): "))
#     if num == 0:
#         break
#     total += num
#
# print("შეყვანილი რიცხვების ჯამი:", total)
# 📌 როგორ მუშაობს:
#
# while True ქმნის უსასრულო ციკლს.
#
# if num == 0: ამოწმებს შეყვანილი რიცხვი ხომ არ არის 0 და break წყვეტს ციკლს.
#
# total += num აჯამებს შეყვანილ რიცხვებს.
#
# გინდა ახლა შემდეგ სავარჯიშოს კოდი? 💡

###---------------------------------------
# სავარჯიშო 2: მხოლოდ კენტები
# შეიყვანე რიცხვები მანამ, სანამ 0-ს არ შეიყვან.
# დაბეჭდე მხოლოდ კენტი რიცხვები.

# while True:
#     num = int(input("შეიყვანე რიცხვი (0-ს შეყვანა დაასრულებს): "))
#     if num == 0:
#         break
#     if num % 2 != 0:
#         print("კენტია:", num)
#--------------------------
# სავარჯიშო:
# შეიყვანე რიცხვები მანამ, სანამ 0-ს არ შეიყვან. იპოვე საშუალო არითმეტიკული.
#
# sum = 0
# count = 0
#
# while True:
#     num = int(input("შეიყვანე რიცხვი (0-ს შეყვანა დაასრულებს): "))
#     if num == 0:
#         break
#     sum += num
#     count += 1
#
# if count > 0:
#     average = sum / count
#     print("საშუალო არითმეტიკული:", average)
# else:
#     print("არ შეყვანილა არცერთი რიცხვ
#---------------------------
# დავთვალოთ საშუალო არითმეტიკული:
# საშუალო =
# რიცხვებისრაოდენობა
# რიცხვებისჯამი
#
# ანუ:საშუალო=  round(3.666..., 1) = 3.7
# round(avg, 1):
# a = int(input("შეიყვანე პირველი რიცხვი: "))
# b = int(input("შეიყვანე მეორე რიცხვი: "))
# c = int(input("შეიყვანე მესამე რიცხვი: "))
#
# avg = (a + b + c) /3
# # print("საშუალო არითმეტიკული:", round(avg, 2))  es gamoyavs3.33  , shemdeg 2 cigri
# print("საშუალო არითმეტიკული:", round(avg, 1))   ama es anu , shemdeg 1 cifri  3.3
# შეიყვანე რიცხვები მანამ, სანამ არ შეიყვან "0".
# დაბეჭდე ყველაზე პატარა რიცხვი,
# რომელიც შეიყვანე.

# min_num = None  # აქ შეინახება ყველაზე პატარა რიცხვი
#
# while True:
#     num = int(input("შეიყვანე რიცხვი (0-ს შეყვანა დაასრულებს): "))
#     if num == 0:
#         break  # ციკლის დასრულება, თუ შეყვანილია 0
#
#     if min_num is None or num < min_num:
#         min_num = num  # განახლება, თუ ახალი რიცხვი პატარაა
#
# if min_num is not None:
#     print("ყველაზე პატარა რიცხვი არის:", min_num)
# else:
#     print("არ შეყვანილა არცერთი რიცხვი.")
#
#//////////////////////////////////////////////

# კენტების და ლუწების დასათვლელად
# count_even = 0  # ლუწების რაოდენობა
# count_odd = 0   # კენტების რაოდენობა
#
# while True:
#     num = int(input("შეიყვანე რიცხვი : "))
#     if num == 0:
#         break  # ციკლის შეწყვეტა, როცა მომხმარებელი 0 შეიყვანს
#
#     if num % 2 == 0:
#         count_even += 1  # ლუწის შემთხვევაში, ვამატებთ ლუწების რაოდენობას
#     else:
#         count_odd += 1   # კენტის შემთხვევაში, ვამატებთ კენტების რაოდენობას
#
# print("ლუწი რიცხვების რაოდენობა:")
# print("კენტი რიცხვების რაოდენობა:")

#--------------------------------------
# max_num = None
#
# while True:
#     num = int(input("შეიყვანე რიცხვი: "))
#     if num == 0:
#         break
#
#     if num > 5:
#         if max_num is None or num > max_num:
#             max_num = num
#
# if max_num is not None:
#     print("ყველაზე დიდი რიცხვი, რომელიც მეტი იყო 5-ზე:", max_num)
# else:
#     print("5-ზე მეტი რიცხვი არ შეყვანილა.")
#
#-------------------------
# count = 0
# max_num = None
#
# while count < 5:
#     num = int(input("შეიყვანე რიცხვი: "))
#     if max_num is None or num > max_num:
#         max_num = num
#     count += 1
#
# print("შეყვანილი 5 რიცხვიდან ყველაზე დიდი არის:", max_num)




















