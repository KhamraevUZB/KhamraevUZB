# IF Operatori

# avtolar = ['audiio','bmw','volvo','kia','hyundai']
# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())


# ism='Ali'
# def nimadur():
#     if ism.lower() == 'ali':
#         return True
#     else:
#         return False
# print(nimadur())

# ism = input('Ismingiz nima?\n>>>') # Foydalanuvchi ismini so'raymiz
# if ism.lower() != 'ali': # Agar ism Aliga teng bo'lmasa ...
#     print(f"Uzr, {ism.title()} biz Alini kutayapmiz.") # quyidagi xabar chiqadi
# else:
#     print("Salom, Ali")

# javob = float(input("12x6 nechiga teng?>>>"))
# if javob!=72:
#     print("Javob xato!")

# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh>=18: # yosh 18 dan katta yoki teng bo'lsa
#     print('Xush kelibsiz!')
# else: # ask holda
#     print('Kirish mumkin emas!')


# login = input("Yangi login tanlang:")
# if len(login)<=5: # login uzunligini tekshiramiz
#     print("Login 5 harfdan ko'proq bo'lishi shart!")

# yil = int(input("Tug'ilgan yilingizni kiriting:"))
# if 2024-yil<18: # foydalanuvchining yoshini hisoblaymiz
#     print(f"Yoshingiz {2024-yil}da ekan.")
#     print("Kirish mumkin emas!")
# else:
#     print("Xush kelibsiz!")

# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")

# x, y = 65, 50 # x=25 va y=50
# print("x>y") if x>y else print("x<y")

# kun = input("Bugun nima kun?>>>")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print('Bugun dam olish kuni.')
# else:
#     print('Bugun ish kuni.')

# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday?"))
# if kun.lower()=='yakshanba' and harorat>=30:
#     print("Cho'milgani ketdik!")
# elif kun.lower()=='yakshanba' and harorat<30:
#     print("Uyda dam olamiz!")