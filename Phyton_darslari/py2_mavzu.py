# Taqqoslash amallari
# >,<, >=, <=, ==, !=, and, or, not
# print("2>3",2>3)
# print("2<3",2<3)
# print("2>=3",2>=3)
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
# if 'solom' in 'salom bolalar':
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

# For operatori

# son=int(input("Sonni kiriting: "))
# while son!=0:
#     print(son%10,end=" ")
#     son//=10

# range(begin, end,step)
# a=100
# b=0
# for i in range(a,b,-1):
#     if i%2!=0:
#         print(i,end=" ")
# str="Salom bolalar"
# for i in str:
#     print(i,end=" ")

# str="Salom bolalar"
# for i in range(0,len(str)):
#     print(str[i],end=" ")

# uchburchak
# for i in range(int(input("n="))):
#     for j in range(i):
#         print(end="* ")
#     print()

# to'rtburchak
# n=int(input("n="))
# for i in range(n):
#     for j in range(n):
#         print(end="* ")
#     print()

# import math

# num = int(input("Sonni kiriting: "))
# is_prime = True

# for i in range(2, int(math.sqrt(num)) + 1):
#     if num % i == 0:
#         is_prime = False
#         break

# if is_prime:
#     print("Tub son:")
# else:
#     print("Son tub emas:")


# String turidagi malumotlar

# str="Salom 72-guruh! Ishlar yaxshimi?"
# for i in str:
#     if i in str:
#         print(i.upper(),end="")
# print()
# print(len(str))


str="Salom 72-guruh! Ishlar yaxshimi?"
# str=str.replace(str,"Hello my dear friends")
print(str)
 
new=""
for i in str:
    if i=='a':
        new+='o'
    elif i=='A':
        new+='O'
    elif i=='O':
        new+='A'
    elif i=='o':
        new+='a'
    else:
        new+=i
str=str.replace(str,new)
print(str)
print(new,type(new))

