# a=int()
# print(a,type(a))
# a=123
# print(a,type(a))
# a=3.1212
# print(a,type(a))
# b=float()
# print(b,type(b))
# c=bool()
# print(c,type(c))
# c=True
# print(c,type(c))



# text='Hello'
# print(text,type(text))
# text1="I'm programmer"
# print(text1,type(text1))
# text2="""Hello Python
# I'm programmer
# I will be softwere developer"""
# print(text2,type(text2))


# CHIQARISH FUNKSIYASI

# print("Hello world",123,3.1415,True,False,end='The end')
# print(12222223)
# a=123
# b=3.1415
# c=True
# d='Foundation'
# print("a=",a,"b=",b,"c=",c,"d=",d)
# print("a={2} b={1} c={0} d={3}".format(a,b,c,d))
# print("a={2} b={2} c={2} d={2}".format(a,b,c,d))
# print("a={:05d} b={:.2f} c={} d={}".format(a,b,c,d))
# print(f"a={a} b={b} c={c} d={d}")


# KIRITISH FUNKSIYASI

# a=int(input("A sonini kiriting: "))
# print("A=",a)
# b=float(input("float sonini kiriting: "))
# print("b=",b)
# c=bool(input("boll tipinin kiriting: "))
# print("c=",c)
# text=input("Textni kiritin: ")
# print("text=",text)

# a=int(input("a="))
# b=int(input("b="))
# print("a+b=",a+b)
# print("a-b=",a-b)
# print("a*b=",a*b)
# print("a/b=",a/b)
# print("a//=b",a//b)
# print("a%b=",a%b)
# print("a**b=",a**b)


# STRING TOIFASI BN ISHLASH

# text="Salom bolalar "
# print(*text)
# print(text*5)
# print(text[0],text[1],text[2],text[3],text[4])
# # [start:finish:step]
# print(text[0:5:2])
# # son+=1
# print(text[0:len(text):3])
# print(text[6:])
# print(text[:5])
# print(text[6:10])
# print(text[::-1])


# SHART VA TAKRORLASH OPERATORLARI

# Taqqoslash amallari

# >,<, >=, <=, ==, !=, and, or, not
# print("2>3",2>3)
# print("2<3",2<3)
# print("2>=3",2>=3)
# print("2<=3",2<=3)
# print("2==3",2==3)
# print("2!=3",2!=3)
# print("2>3 and 1<2",2>3 and 1<2)
# print("2>3 or 1<2",2>3 or 1<2)
# print("not(2>3 and 1<2)",not(2>3 and 1<2))


#shart operatorlari

# a=int(input("a sonini kiriting: "))
# if a>0:
#     print("MUSBAT")
#     print("Hello")
# elif a<0:
#     print("MANFIY")
#     print("Salom")
# else:
#     print("Son 0 ga")
#     print("Ola amigo")

# In funksiyasi va while operatori

# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# d=int(input("d="))
# max=a
# if b>max:
#     max=b
# if c>max:
#     max=c
# if d>max:
#     max=d
# print(max)


# if 'a' in 'salom bolalar':
#     print("a harfi bor")
# else:
#     print("a harfi yoq")
# if 'salom' in 'salom bolalar':
#     print("Bor")
# else:
#     print("Yoq")



# while operatori

# num=0
# while 1:
#     num+=1
#     if num==4 or num==6:
#         continue
#     print(num,end=" ")
#     if num==10:
#         break

# i=1
# while i<=10:
#     print(i,end=" ")
#     i+=1
#     if i==11:
#         break

# For operatori

# son=int(input("Sonni kiriting: "))
# while son!=0:
#     print(son%10,end=" ")
#     son//=10

# for i in range(1,10):
#     print(i,end=" ")    

# str="Salom bolalar"
# for i in range(0,len(str)):
#     print(str[i],end='')

# for i in range(int(input("n="))):
#     for j in range(i):
#         print(end='* ')
#     print()


# n = int(input("n="))

# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(end='  ')
#     for j in range(i):
#         print('*', end=' ')
#     print()

# n=10
# for i in range(n):
#     print('' * (n - i) + '* ' * i)


# def uchburchakL(n):
#     for i in range(1,n+1):
#         print("* " * i)
# def uchburchakR(n):
#     for i in range(1,n):
#         print('    ' * (n-i) + "* "*i)
# def uchburchak_downL(n):
#     for i in range(n,0,-1):
#         print('    ' * (n-i) + "* " * i)
# def uchburchak_downR(n):
#     for i in range(n,0,-1):
#         print("* " * i)
# n=10
# uchburchakL(n)
# uchburchak_downR(n)
# uchburchakR(n)
# uchburchak_downL(n)


# list1=list()
# list2=[]
# list3=[123,3.1415,'salom',True,False,2.72,"hayr"]
# print(*list3)
# list3.append(100)
# for i in list3:
#     print(i)
# list3.insert(1,'hello')
# list3.clear()
# list3.pop(1)
# list3.remove(True)


# print(list3)


# list=[1,2,23,3,34,45,45,456,56,5,645,45,345,34,35,45,4,3,333,33,5,46,5,456]
# print(list.count(5))
# print(list.index(56))
# list.reverse()
# list.sort(reverse=True)
# print(list)


# list=['salom','qalaysan','ishlar','joyidami']
# list1=[1,2,7,4,9,0,8,5,3,6]
# list1.sort()
# print(*list1)
# list1.sort(reverse=True)
# print(*list1)
# list.sort(reverse=True)
# print(*list)
# list.sort()
# print(*list)


# TUPLE bilan ishlash

# list1=[[1,2,3],[4,5,6],[7,8,9]]
# for i,j,k in list1:
#     print(i,j,k)

# list1=[1,2,3,4,5,0,0]
# list2=[6,7,8,9,0]
# list3=list1+list2
# print(*list3)
# for i in range(0,len(list3),4):
#     print(list3[i], list3[i+1],list3[i+2], list3[i+3])
# 
# for i in range(1,10):
#     for j in range(1,10):
#         print(f"{i} * {j} = {i*j}")
#     print()



# count=0
# while True:
#     print(count)
#     count+=1
#     if count>5:
#         break
# for i in range(10):
#     if not i%2!=0:
#         continue
#     print(i,end=' ')

# count=0
# for i in range(1,10):
#     if(i%6==0):
#         break
#     print(i)


# ls=[("salom",15),("hayr",1),("bolalar",5)]
# for i in ls:
#     print(*i)
# for i in range(len(ls)):
#     print(ls[i])
#     for j in range(i+1,len(ls)):
#         if ls[i][1]>ls[j][1]:
#             ls[i],ls[j]=ls[j],ls[i]
# print("=================")
# for i in ls:
#     print(*i)
# print(ls[1][0])


# ls=[("salom",15),("hayr",1),("bolalar",5)]
# for i in ls:
#     print(*i)
# son=int(input("sonni kiriting: "))
# t=list(ls[1])
# t[1]=son
# ls[1]=tuple(t)
# for i in ls:
#     print(*i)



# SET MAVZUSI


# s1=set()
# s2={1,2,4,1,1,1,12,2,3,4,2,4,1,12}
# s2.add(-5)
# print(s2)
# s1=s2.copy()
# print(s1)
# print(s2)


# s1={1,2,3,4,5}
# s2={4,5,6,7,8,9}
# print(s1.difference(s2))  # s1 dagi s2 da yo'q ma'lumotlarni ko'rsatadi
# print(s2.difference(s1))  # s2 dagi s1 da yo'q ma'lumotlarni ko'rsatadi
# s1.difference_update(s2)  # s1 dagi s2 da takrorlangan ma'lumotlarni o'chiradi
# s2.difference_update(s1)    # s2 dagi s1 da takrorlangan ma'lumotlarni o'chiradi
# print(s1,s2)
# s1.update(s2)   # s1 ga s2 ni malumotlarini update qilib qo'shadi
# print(s1.intersection(s2))  # s1 va s2 dagi bir xil elementlarni chiqarib beradi
# s1.intersection_update(s2)  # s1 va s2 dagi oxshash ma'lumotlarni s1 ga saqlaydi va print funkiyasining ichida ishlamaydi
# print(s1.union(s2),s2)  # s1 ga s2 dagi takrorlanmaydigan ma'lumotlarni o'tkazadi faqat printda
# s1.discard(4)  # maumotni ichidan qiymatni uchirib tashlaydi
# s1.pop()   # pop setning boshidagi ma'lumotni uchirib tashlaydi
# print(s1,s2)

#  SET VA LIST MA'LUMOTLARI BILAN ISHLASH

# ls=[{1,2,3},{1,4,5},{2,1,3},{4,2,1}]
# nl=list()
# for i,j,k in ls:
#     nl.append(i)
#     nl.append(j)
#     nl.append(k)
# print(*nl)


# DICTIONARY tartiblangan set ma'lumotlari

# d1=dict()
# print(d1,type(d1))
# d2={1:"salom","hayr":123,False:True,1:'hello'}
# print(d2.keys())
# print(d2.values())
# print(d2.items())
# d1.update(d2)
# print(d1)
# d1=d2.copy()
# print(d1)
# print(d2.get("hayr")) # kalit ostidagi qiymatni chiqarib beradi
# d2.pop(1)
# d2.popitem()
# print(d2)

# DICTIONARY VA LIST MA'LUMOTLARI BILAN ISHLASH

# l1=[1,2,3]
# l2=["John","Smith","Adam"]
# l3=[0.1,0.2,0.3]
# ls=[]
# for i in range(len(l1)):
#     ls.append({l1[i]:{l2[i]:l3[i]}})
# print(ls)

# d1={'a':1,'b':2,'c':3}
# st=str()
# for i in d1.keys():
#     st+=i*d1[i]
# print(st)
# d1['d']=4
# print(d1)

# FUNKSIYA MAVZUSI

# def summary(a,b):
#     print(a,"+",b,"=",a+b)
# summary(1,2)
# summary(3.1415,3.1415)
# summary(True,2.73)
# summary("salom",'bolalar')

# def calculate(a,b):
#     return [a+b,a-b,a/b,a//b,a%b,a**b]
# print(*calculate(2,3))


# def salomlashish():
#     print(10*"salom ")
# def hayrlashish():
#     return 5*"hayr "
# def main():
#     salomlashish()
#     print(hayrlashish())
# main()


# ITERATIV FUNCSION

# def enter_list(sonlar):
#     for i in range(int(input("n= "))):
#         sonlar.append(input("---> "))
# ls=[]
# enter_list(ls)
# print(ls)

# rekursiv function

# def fact(n):
#     if n==0:
#         return 1
#     elif n>0:
#         return n*fact(n-1)
# print(fact(int(input("son= "))))

# def teskari(son):
#     if son>0:
#         print(son%10,end=' ')
#         teskari(son//10)
#     else:
#         print()
# teskari(int(input("son= ")))
# def togri(son):
#     if son>0:
#         togri(son//10)
#         print(son%10,end=' ')
# togri(int(input("son= ")))

# def func(a,b):
#     return a+b
# print(func(2,3))
# x=lambda a,b: a+b
# print(x(2,3))
# def oma(a,b):
#     print(a+b)
# oma(2,3)
# x=lambda a,b: print(a+b)
# x(2,3)  

# ish="Salom dasturchilar"
# (lambda a:print(a))(ish*2)


# Modullar mavzusi

# import math as m
# print(m.factorial(5))
# print(m.fabs(-2.34))
# print(m.sqrt(100))
# from math import *
# print(round(2.5))
# print(pow(10,3))
# print(fmod(12.12,10))
# print(12.12%10)

# Random modullari

# import random as r
# print(r.randint(1,5))  # [1,5] oraligidagi sonlar
# print(r.random()*100)      # [o.o,1.0] oraligidagi sonlar  agar *100 quyilsa 0 dam 100 gacha float sonlarini ciqarib beradi
# print(r.randrange(1,10,2))  # [1,3,5,7,9]
# ls=[i for i  in range(1,11)]
# r.shuffle(ls)
# print(*ls)
# print(r.choice(ls))


# import time 
# print(3)
# time.sleep(1)
# print(2)
# time.sleep(1)
# print(1)
# time.sleep(1)
# print(0)
# time.sleep(1)
# print("BUUUUUM!!!!!!")
# print(time.asctime())  #real time


# colorama moduli


# import colorama as c 
# print(c.Fore.RED,"Salom bolalar")
# print('Hello')
# print(c.Back.BLUE,"Hello")



# Istisnolar bilan ishlash

# try:
#     print(2/1)
# except:
#     print("bo'lishdagi xatoliklar")
# else:
#     print("xatolik topilmadi")
# finally:
#     print("tekshiruv tugadi")


# try:
#     raise NameError("Nomini e'lon qilishdagi xatolik")
# except:
#     raise



lugat={'sabzi':'gilos','olma':'shaftoli'}
print(lugat['olma'])
print(lugat['sabzi'])