# 3-mavzu: Data structures (list, tuple, set, dictionary)

# Uyga vazifa:
# 1) Bizga list berilgan va foydalanuchi tomonidan bitta son kiritiladi. Agarda ikkta elementining 
# yig'indisi kiritilgan songa teng bo'lsa shu elementlarning index’larini ekranga chiqaruvchi dastur tuzing.
# lst = [1, 2, 33, 5, 6, 7, 7]
# INPUT = 3
# lst[0]+lst[1] = 3
# OUTPUT = 0 , 1
# INPUT = 8
# lst[0]+lst[5] = 8
# lst[0]+lst[6] = 8
# OUTPUT = 0 , 5 va 0,6



# lst = [1, 2, 33, 5, 6, 7, 7]
# a=int(input("sonni kiriting "))
# caunt=int()
# for i in range(len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i]+lst[j]==a:
#             print(i,j)



# 2) input orqali gap kiritiladi shu gapdagi so'zlarni bosh harfi orqali alfabet tartibida chiqarish kerak.
# input: salom aziz qalaysan
# output: aziz qalaysan salom

# text=input("Gapni kiriting: ")
# print("INPUT: ",text)
# text1=text.split()
# text1.sort()
# print("OUTPUT: ",*text1)



# 3) Kiritilgan songacha bo'lgan sonlar yig'indisini quyidagi ko'rinishda ekranga chiqarilsin:
# input: 6
# output: 1+2+3+4+5+6=21
# input: 4
# output: 1+2+3+4=10

# son=int(input("Sonni kiriting: "))
# son1=1
# for i in range(2,son+1):
#     son1+=i
# print(son1)


# n = int(input("Sonni kiriting: "))
# sum_of_numbers = 0
# output_string = ""
# for i in range(1, n + 1):
#     sum_of_numbers += i
#     if i == n:
#         output_string += str(i)
#     else:
#         output_string += str(i) + "+"
# output_string += "=" + str(sum_of_numbers)
# print(output_string)


# 4) Kiritilgan gapdagi toq uzunlikdagi so'zlarni teskarisiga yozilsin. Juft uzunlikdagilari esa shundoq qolsin.
# input: salom aziz nima gap
# output: molas aziz nima pag

# text=input("Gapni kiriting: ")
# text1=text.split()
# text3=[]
# for i in text1:
#     if len(i)%2==1:
#         text3.append(i[::-1])
#     else:
#         text3.append(i)
# natija=' '.join(text3)
# print(natija)


# 5) Kiritilgan soning ikkilik sanoq sistemasiga o'tkazilgandagi nollar sonini topish:
# input: 12
# output: 2


# son=int(input("Sonni kiriting: "))
# binary_korinishi=bin(son)[2:]
# zero=binary_korinishi.count('0')
# print(zero)
# print(binary_korinishi)


# 6) Kiritilgan sondan keyingi 5ta tub sonni topuvchi dastur tuzing.
# input: 20
# output: 23 29 31 37 41


# son = int(input("Sonni kiriting: "))
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# prime_numbers = []
# number = son + 1
# while len(prime_numbers) < 5:
#     if is_prime(number):
#         prime_numbers.append(number)
#     number += 1
# print(" ".join(map(str, prime_numbers)))


# 7) Foydalanuchi so'z va harf kiritadi agar kiritilgan harf so'zda bo'lsa, o'sha harfni kattaga almashtirish. Masalan:
# input1: salomlar
# input2: a
# Natija: sAlomlAr

# def kattalashtirish(soz, harf):
#     natija = ''
#     for belgi in soz:
#         if belgi == harf:
#             natija += belgi.upper()
#         else:
#             natija += belgi
#     return natija

# text=input("So'zni kiriting: ")
# harf=input("Harfni kiriting: ")
# natija = kattalashtirish(text, harf)
# print(f"Natija: {natija}")

# 8) 2+22+222+....+n n gacha sonlar yig'indisni toping. n foydalanuvchi tomonidan kiritiladi.
# input: n=5
# output: 2+22+222+2222+22222=24690
# input: n=3
# output: 2+22+222=246


# def sonlar_yigindisi(n):
#     yigindi = 0
#     current_number = 2
#     for i in range(1, n + 1):
#         yigindi += current_number
#         if i < n:
#             print(f"{current_number} + ", end="")
#         else:
#             print(f"{current_number}", end="")
#         current_number = current_number * 10 + 2
#     print(f" = {yigindi}")
#     return yigindi
# n = int(input("n = "))
# natija = sonlar_yigindisi(n)
# print(f"Natija: {natija}")


# 9) O'nlik sanoq sistemasida yozilishida ikkita bir xil raqami bo'lmagan barcha to'rt xonali natural sonlar ekranga chiqariluvchi dastur yarating.

# def tort_xonali_nat_sonlar():
#     count = 0
#     for num in range(1000, 10000):
#         num_str = str(num)
#         if len(set(num_str)) == len(num_str): 
#             print(num_str)
#             count += 1
#     print(f"Jami {count} ta to'rt xonali natural son topildi.")


# print("To'rt xonali natural sonlar:")
# tort_xonali_nat_sonlar()


# 10) Foydalanuvchi istlagan xonali son kiritadi va sizning vazifangiz ushbu sonni birliklar, o’nliklar, yuzliklar va hokazo xonalar yig’indisi yoyilmasiga aylantirib chiqaradigan dastur tuzish.
# input: 123     input: 4213
# output: 100+20+3   output: 4000+200+10+3

# def son_yigindisi(son):
#     son_str = str(son)
#     uzunlik = len(son_str)
#     yigindi = ""
    
#     for i, raqam in enumerate(son_str):
#         katta_son = int(raqam) * 10**(uzunlik - i - 1)
#         if i < uzunlik - 1:
#             yigindi += f"{katta_son} + "
#         else:
#             yigindi += f"{katta_son}"
#     print(f"Natija: {yigindi}")
# son = int(input("Istalgan sonni kiriting: "))
# son_yigindisi(son)


# 11) Son kiritiladi shu sonni tub bo'luvchilarga ajratib chiqarib beradigan dastur tuzing.
# input: 34   input: 24    input: 225
# output: [2,17]  output: [2,2,2,3]  output: [3,3,5,5]


# def tub_boluvchilar(son):
#     boluvchilar = []
#     i = 2
#     while son > 1:
#         if son % i == 0:
#             boluvchilar.append(i)
#             son //= i
#         else:
#             i += 1
#     return boluvchilar
# son = int(input("Sonni kiriting: "))
# natija = tub_boluvchilar(son)
# print(f"Natija: {natija}")

# 12) Foydalanuchi tomonidan list kiritiladi. Shu listni kombinatsiyalarini quyidagi ko'rinishda ekranga chiqaruvchi dastur yarating.
# INPUT = [1, 2 ,3]
# OUTPUT = [[1, 2, 3] , [3, 2, 1] ,[1, 3, 2] ,[3, 1, 2] ,[2, 1, 3] ,[2, 3, 1] ]
# INPUT = [0, 1]
# OUTPUT = [[0, 1] , [1, 0]]


# import itertools

# def list_kombinatsiyalari(lst):
#     kombinatsiyalar = list(itertools.permutations(lst))
#     return kombinatsiyalar
# input_list = eval(input("Listni kiriting: "))
# natija = list_kombinatsiyalari(input_list)
# print(f"Natija: {natija}")

# 13) Listdagi o'sish tardibida kelgan sonlar to'plamini hisoblash. 
# Masalan lst = [1, 3, 4, 9, 3, 4, 0, -1, 7, 8 ]
# Bu listda o'sish tardibida kelgan to'plamlar bu 
# " 1, 3, 4, 9 "
# " 3, 4 "
# " -1, 7, 8 "
# Ularning soni 3ta


# def o_sish_tardibida_kelgan_toplamlar(lst):
#     o_sish_tardibida_kelgan_toplamlar = []
#     toplam = [lst[0]]
#     for i in range(1, len(lst)):
#         if lst[i] >= lst[i - 1]:
#             toplam.append(lst[i])
#         else:
#             o_sish_tardibida_kelgan_toplamlar.append(toplam)
#             toplam = [lst[i]]
#     o_sish_tardibida_kelgan_toplamlar.append(toplam)
#     return o_sish_tardibida_kelgan_toplamlar
# lst = [1, 3, 4, 9, 3, 4, 0, -1, 7, 8]
# natija = o_sish_tardibida_kelgan_toplamlar(lst)
# print(f"Listdagi o'sish tardibida kelgan to'plamlar: {natija}")
# print(f"Ularning soni: {len(natija)}")
