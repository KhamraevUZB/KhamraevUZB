# 5-mavzu: Modul va istisno(Exception)

# Uyga vazifa:
# 1) Text’ni input orqali kiriting va ushbu text’dagi harflarni rangli chiqaring.
# AaBbCcDdEeFfGgHh - qizil rangda
# IiJjKkLlMmNnOoPp - sariq rangda
# QqRrSsTtUuVvWwXxYyZz - yashil rangda


# from colorama import Fore,init
# init(autoreset=True)
# def color_text(s):
#     qizillar="AaBbCcDdEeFfGgHh"
#     sariqlar="IiJjKkLlMmNnOoPp"
#     yashillar="QqRrSsTtUuVvWwXxYyZz"
#     rangli_yozuv=""
#     for i in s:
#         if i in qizillar:
#             rangli_yozuv+=Fore.RED+i
#         elif i in sariqlar:
#             rangli_yozuv+=Fore.YELLOW+i
#         elif i in yashillar:
#             rangli_yozuv+=Fore.GREEN+i
#         else:
#             rangli_yozuv+=i
#     return rangli_yozuv
# soz=input("so'zni kiriting: ")
# print(color_text(soz))


# 2) Sezar metodini shifrlaydigan dastur tuzing. Ya'ni Sezar metodi bu 0dan 10gacha sonlar ketma-ketligidagi sonlarning oxirgi uchtasini boshiga o'tkazadi. Ya'ni:
# Oddiy sonlar:  0 1 2 3 4 5 6 7 8 9
# Sezar sonlari: 7 8 9 0 1 2 3 4 5 6
# Input:   1946
# Output:  8613
# Input:   10023
# Output:  87790



# def func(number):
#     oddiy = "0123456789"
#     sezar = "7890123456"
#     natija = ""
#     for i in str(number):
#         index = oddiy.index(i)
#         natija += sezar[index]
#     return natija
# print(func("1946")) 
# print(func("10023")) 



# 3) 100ta sondan iborat Listga 100dan 1000gacha bo’lgan sonlar random to’ldirilgan. 
# Ushbu listdagi qiymatlar orasidan tasodifiy bittasi N ga olindi va sizning vazifangiz ushbu 
# N sonigacha bo’lgan sonlar orasidan juftlarini chiqaring. 

# import random
# random_list = [random.randint(100, 1000) for _ in range(100)]
# N = random.choice(random_list)
# even_numbers = [num for num in range(N) if num % 2 == 0]
# print("Tasodifiy tanlangan N:", N)
# print("N sonigacha bo'lgan juft sonlar:", even_numbers)


# 4) 1000ta sondan iborat Listga 1dan 1000000gacha bo’lgan sonlar random to’ldirilgan. 
# Ushbu listdagi qiymatlar orasidan tasodifiy bittasi N ga olindi va sizning vazifangiz ushbu 
# N sonidan keyin kelgan sonlar orasidan tublarini chiqaring. 


# import random
# import math
# random_list=[random.randint(1,1000000)for _ in range(1000)]
# N = random.choice(random_list)
# print(N)
# for i in range(N,1000000):
#     prime = 1
#     for j in range(2, int(math.sqrt(i)) + 1):
#         if i%j==0:
#             prime=0
#             break
#     if prime==1:
#         print(i,end=" ")



# 5) Foydalanuvchi ketma-ket istalgan miqdorda int tipidagi 
# sonlarni c harfini kiritmaguncha kiritadi. 
# Maqsadingiz shu sonlar yig'indisini topish.
# Output
# Enter numbers [c for cancel]:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# c
# Sum of 10 numbers: 55



# def sum_numbers():
#     total_sum = 0
#     count = 0
    
#     print("Enter numbers [c for cancel]:")
    
#     while True:
#         user_input = input()
        
#         if user_input.lower() == 'c':
#             break
        
#         try:
#             number = int(user_input)
#             total_sum += number
#             count += 1
#         except ValueError:
#             print("Invalid input, please enter an integer or 'c' to cancel.")
    
#     print(f"Sum of {count} numbers: {total_sum}")

# sum_numbers()

# 6) Foydalanuvchi ketma-ket istalgan miqdorda string tipidagi so’zlarni raqamni kiritmaguncha kiritadi. Maqsadingiz shu so’zlarni bitta matn sifatida yig’ish. Har bir gap bosh harf bilan boshlanadi va har bir 5ta so’zdan keyin ‘.’(nuqta) qo’yiladi.
# Output
# Enter numbers [0 for cancel]:
# salom
# foundation
# N10
# guruhi
# o’quvchilari
# imtihon
# natijalariga
# ko’ra
# guruhingiz
# o’tdi
# hammani tabriklaymiz
# 0
# Matn: Salom foundation N10 guruhi o’quvchilari. Imtihon natijalariga ko’ra guruhingiz o’tdi. Hammani tabriklaymiz


    
def collect_sentences():
    words = []
    print("Enter words [0 for cancel]:")
    
    while True:
        word = input()
        
        if word == '0':
            break
        
        words.append(word)
    
    # Gaplarni yig'ish
    sentences = []
    sentence = ""
    
    for i in range(len(words)):
        if i > 0 and i % 5 == 0:
            sentences.append(sentence.strip().capitalize() + '.')
            sentence = ""
        
        sentence += words[i] + " "
    
    if sentence:
        sentences.append(sentence.strip().capitalize() + '.')
    
    final_text = " ".join(sentences)
    print("Matn:", final_text)

collect_sentences()


