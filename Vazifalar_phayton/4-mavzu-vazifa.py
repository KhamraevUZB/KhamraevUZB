# 4-mavzu: Funksiya va rekursiya 

# Uyga vazifa:
# 1) Funksiya orqali 3ta listni ma'lumotlarini bitta listga birlashtirish kerak. Ya'ni 1-list ma'lumoti dictionary’ning key’si bo'ladi va 2-list va 3-list ma'lumotlari esa alohida dictionary’ning key’si va value’si bo'ladi.
# Input:
# ['S001', 'S002', 'S003', 'S004']
# ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# [85, 98, 89, 92]
# Output:
# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
 

# def vazifa(ls1,ls2,ls3):
#     ls=[]
#     for i in range(len(ls1)):
#         ls.append({ls1[i]: {ls2[i]:ls3[i]}})
#     return ls
# ls1=['S001', 'S002', 'S003', 'S004']
# ls2=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# ls3=[85, 98, 89, 92]
# print(vazifa(ls1, ls2, ls3))


# 2) Funksiya orqali Kiritilgan string ma'lumotini dictionary;ga har bir belgi key’ga va ushbu belgi nechtaligi value’ga yozilsin.
# Input: 'w3resource'
# Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}


# def func(s):
#     count = {}
#     for i in s:
#         if i in count:
#             count[i] += 1
#         else:
#             count[i] = 1
#     return count
# string=input("string malumotini kiriting: ")
# print(func(string))



# 3) Funksiya orqali Dictionary berilgan ushbu dictionary’da kaliti juft o’rindagi qiymatlarni kaliti toq o’rindagi bilan almashtiradigan va chiqaradigan funksiya yarating. 
# Input (Kiruvchi ma’lumotlar):
# dict1={1:ABC, 2:DEF, 3:GHI, 4:JKL, 5:MNO}
# Output (Chiquvchi ma’lumotlar):
# dict1={1:DEF, 2:ABC, 3:JKL, 4:GHI, 5:MNO}

# def kirish(s):
#     keys = list(s.keys())
#     for i in range(0, len(keys) - 1, 2):
#         if i + 1 < len(keys):
#             s[keys[i]], s[keys[i + 1]] = s[keys[i + 1]], s[keys[i]]
#     return s
# dict1 = {1: 'ABC', 2: 'DEF', 3: 'GHI', 4: 'JKL', 5: 'MNO'}
# print(kirish(dict1))



# 4) Funksiya orqali String’ga bir nechta so'z va gaplar berilgan. Ushbu string’dagi ma'lumotlarni so'zlarni va gaplarni alohida listlarga joylashtiradigan funksiya tuzing.
# Input: Salom Yoz. Olam juda ham go’zal. Imtihon bo’lyapti.
# Output:
# words: [Salom, Yoz, Olam, juda, ham, go’zal, Imtihon, bo’lyapti]
# sentence: [Salom Yoz, Olam juda ham go’zal, Imtihon bo’lyapti]




# def spl(s):
#     soz = s.replace('.','').split()
#     jumla = s.split('. ')
#     jumla = [gap.strip('.') for gap in jumla if gap]
#     return soz, jumla
# input_string = "Salom Yoz. Olam juda ham go’zal. Imtihon bo’lyapti."
# soz,jumla=spl(input_string)
# print("words:",soz)
# print("sentence:",jumla)


# 5) Funksiya orqali Listga bir nechta sonlar kiritilgan va sizning vazifangiz ushbu sonlardan eng katta son yasash.
# Input (Kiruvchi ma’lumotlar):
# [1, 2, 3]
# [61, 228, 9]
# Output (Chiquvchi ma’lumotlar): 
# 321
# 961228



# def compare(a, b):
#     return (a + b) > (b + a)

# def largest_number(nums):
#     str_nums = list(map(str, nums))
    
#     n = len(str_nums)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if not compare(str_nums[j], str_nums[j+1]):
#                 str_nums[j], str_nums[j+1] = str_nums[j+1], str_nums[j]
    
#     largest_num = ''.join(str_nums)
#     return largest_num

# input1 = [1, 2, 3]
# input2 = [61, 228, 9]

# output1 = largest_number(input1)
# output2 = largest_number(input2)

# print("Output1:", output1)
# print("Output2:", output2)



# 6) Funksiya orqali listni ichida list berilgan. Ichki listlar 3ta ma'lumotdan iborat. Ushbu listni dictionary’ga o'tkazing.
# Input:
# [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
# Output:
# {1: ['Jean Castro', 'V'], 2: ['Lula Powell', 'V'], 3: ['Brian Howell', 'VI'], 4: ['Lynne Foster', 'VI'], 5: ['Zachary Simon', 'VII']}




# def lugat(lst):
#     dict={}
#     for i in lst:
#         kalit=i[0]
#         qiymat=i[1:]
#         dict[kalit]=qiymat
#     return dict
# lst=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
# print(lugat(lst))


# 7) Funksiya orqali listda bir nechta sonlarni input orqali kiriting va ushbu sonlar orasidan 1-raqami juft bo'lganlarni chiqaring.
# Input: [123, 456, 789, 852, 12, 42, 61, 369]
# Output: 456 852 42 61




# def raqamlar(s):
#     natija=[]
#     for i in s:
#         birinchi_son=int(str(i)[0])
#         if birinchi_son%2==0:
#             natija.append(i)
#     return natija
# input_list = [123, 456, 789, 852, 12, 42, 61, 369]
# print("Output: ",*raqamlar(input_list))


# 8) Lamb’da funksiya orqali kiritilgan listning kvadratini chiqaruvchi funksiya yozing.
# Input: [1,2,3,4,5,6,7,8,9,10]
# Output: [1,4,9,16,25,36,49,64,81,100]




# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# square = list(map(lambda a: a**2,numbers))
# print(square)



# 9) Lamb’da funksiyasi orqali listni ichidagi tuple’ning ma'lumotlarning 2 elementi bo'yicha o'sish tartibida saralang.
# Input:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Output:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]



# input_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# sorted_list = sorted(input_list, key=lambda x: x[1])
# print("Output:", sorted_list)




# 10) Lamb’da funksiyasi orqali listni juft va toqlarga ajrating.
# Input:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Juft: [2, 4, 6, 8, 10]
# Toq: [1, 3, 5, 7, 9]


# input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = list(filter(lambda x: x % 2 == 0, input_list))
# odd_numbers = list(filter(lambda x: x % 2 != 0, input_list))
# print("Juft:", even_numbers)
# print("Toq:", odd_numbers)


# 11) String’da son berilgan va ushbu sonning boshida nechta 0 (nol) qatnashganini aniqlaydigan funksiya tuzing.
# INPUT (Kiruvchi ma'lumotlar): '100'
# OUTPUT (Chiquvchi ma'lumotlar):  0
# INPUT (Kiruvchi ma'lumotlar): '001'
# OUTPUT (Chiquvchi ma'lumotlar):  2
# INPUT (Kiruvchi ma'lumotlar): '100100'
# OUTPUT (Chiquvchi ma'lumotlar):  0
# INPUT (Kiruvchi ma'lumotlar): '001001'
# OUTPUT (Chiquvchi ma'lumotlar):  2
# INPUT (Kiruvchi ma'lumotlar): '012345679'
# OUTPUT (Chiquvchi ma'lumotlar):  1
# INPUT (Kiruvchi ma'lumotlar): '0000'
# OUTPUT (Chiquvchi ma'lumotlar):  4


# def hisob(a):
#     count=0
#     for i in a:
#         if i=='0':
#             count+=1
#         else:
#             break
#     return count
# son=input("sonni kiriting: ")
# print(hisob(son))

# 5-masala. Kompyuter sana va vaqt formati faqat raqamlardan iborat, masalan:
#  21.05.2018 16:30 Insonlar shunday narsalarni ko'rishni afzal ko'radilar:
#  2018 yil 21 may, 16 soat 30 daqiqa Sizning vazifangiz oddiy - kiritilgan sana va
#  vaqtni kompyuter formatidan "inson" formatiga aylantiradigan funksiya tuzish. 
# INPUT(Kiruvchi ma'lumotlar):  "01.01.2000 00:00"
# OUTPUT (Chiquvchi ma'lumotlar):    "1 January 2000 year 0 hours 0 minutes"
# INPUT (Kiruvchi ma'lumotlar):  "19.09.2999 01:59"
# OUTPUT (Chiquvchi ma'lumotlar):    "19 September 2999 year 1 hour 59 minutes"
# INPUT (Kiruvchi ma'lumotlar):  "21.10.1999 18:01"
# OUTPUT (Chiquvchi ma'lumotlar):    "21 October 1999 year 18 hours 1 minute"



# def format_datetime(dt_str):
#     import calendar
#     date_part, time_part = dt_str.split()
#     day, month, year = map(int, date_part.split('.'))
#     hour, minute = map(int, time_part.split(':'))
#     months = list(calendar.month_name[1:])
#     month_name = months[month - 1]
#     year_str = f"{year} year"
#     hour_str = f"{hour} hour" if hour == 1 else f"{hour} hours"
#     minute_str = f"{minute} minute" if minute == 1 else f"{minute} minutes"
#     return f"{day} {month_name} {year_str} {hour_str} {minute_str}"
# son=input("sonani kiriting: ")
# print(format_datetime(son))

