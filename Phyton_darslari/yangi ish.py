# text="hello"
# print(text,type(text))
# text2="I'm a programmer"
# print(text2,type(text2))
# text3="""Hello guys
# I'll be 
# IT Devoloper"""
# print(text3)

# print("Hello world",123,3.1415,True,False,sep=' ')
# print(12345678909)
# a=123
# b=3.1415
# c=True
# d='foundation'
# print("a=",a,"b=",b,"c=",c,"d=",d)
# print("a={} b={} c={} d={}".format(a,b,c,d))

# a=int(input("int sonini kiriting: "))
# print("a=",a)
# b=float(input("float sonini kiriting: "))
# print("b=",b)
# c=bool(input("bool tipini kiriting: "))
# print("c=",c)
# text=input("textni kiriting:")
# print("text=",text)

# a=int(input("a="))
# b=int(input("b="))
# print("a+b=",a+b)
# print("a-b=",a-b)
# print("a*b=",a*b)
# print("a/b=",a/b)
# print("a//b=",a//b)
# print("a%b=",a%b)
# print("a**b=",a**b)

# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# d=int(input("c="))
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
# if 'salom' in 'salom bolaral':
#     print("bor")
# else:
#     print("yo'q")

# i=1
# fact=1
# n=int(input("n="))
# while i<=n:
#     fact=fact*i
#     i=i+1
# print(fact)
# print(str(n)+"!="+str(fact))

# son=int(input("sonni kiritin: "))
# while son!=0:
#     print(son%10,end=" ")
#     son//=10


# for i in range(1,10):
#     for j in range(1,10):
#         print(f"{i}*{j}={i*j}") 
#     print()

# i=int(input("Birinchi sonni kiriting: "))
# j=int(input("Ikkinchi sonni kiriting: "))
# print(f"{i}*{j}={i*j}")

# for i in range(1,11):
#     print(i,end=" ")


# list1=list()
# list2=[]
# list3=[123,3.1415,'salom',True,False,2.73,'hayr']
# list3.append(100)
# list3.insert(1,'hello')
# list3.pop()
# list3.remove(True)
# list3,caunt()
# print(list3)
# list1=[1,1,1,2,2,2,3,3,5,2,12,2,1,12,1]
# print(list1.count(1))
# print(list1.index(2))
# list1.reverse()
# print(list1)
# list1.sort(reverse=True)
# print(list1)

# list1=['salom','qalaysiz','ishlar yaxshimi','alik']
# list1.sort()
# print(list1)
# list1.sort(reverse=True)
# print(list1)

# list=[[1,2,3],[4,5,6],[7,8,9]]
# for i,j,k in list:
#     print(i,j,k)

# list1=[1,2,3,4,5]
# list2=[6,7,8,9,10]
# print(list1+list2)

# a=12
# a=float(a)
# print(a,type(a))

# t1=tuple()
# t2=()
# t3=(1,2,3,True,False,'salom','hayr')
# print(t3.count(1))
# print(t3.index(False))

# ls=[("salom",15),("hayr",1),("bolalar",5)]
# for i in range(len(ls)):
#     for j in range(i+1,len(ls)):
#         if ls[i][1]<ls[j][1]:
#             ls[i],ls[j]=ls[j],ls[i]
# for i in ls:
#     print(*i)

# ls=[("salom",15),("hayr",1),("bolalar",5)]
# for i in ls:
#     print(*i)
# son=int(input("son="))
# for i in range(len(ls)):
#     t=list(ls[i])
#     t[1]=son
#     ls[i]=tuple(t)
# for i in ls:
#     print(*i)

# s1=set()
# s2={1,2,4,1,1,1,12,2,3,4,2,4,1,12}
# s2.add(-5)
# print(s2)
# s1=s2.copy()
# print(s1)

# s1={1,2,3,4,5}
# s2={4,5,6,7,8,9}
# print(s1.difference(s2))
# print(s2.difference(s1))
# s2.difference_update(s1)
# print(s1,s2)
# s2.update(s1)
# print(s1,s2)
# print(s1.intersection(s2))
# print(s1.union(s2))
# print(s1)
# s1.discard(4)
# print(s1)
# s1.pop()
# print(s1)

# ls=[{1,2,3},{1,4,5},{2,1,3},{4,2,1}]
# nl=list()
# for i,j,k in ls:
#     nl.append(i)
#     nl.append(j)
#     nl.append(k)
# print(nl)

# ls=[1,2,3,4,5]
# t=1,2,3,4,5
# s={1,2,3,4,5}
# for i in range(len(ls)):
#     print(s[i],end=" ")

# d1=dict()
# print(d1,type(d1))
# d2={1:'salom',"hayr":123,False:True,123:'hello'}
# print(d2.get(1))
# d2.clear()
# print(d2)

# l1=[1,2,3]
# l2=["John","Smith","Adam"]
# l3=[0.1,0.2,0.3]
# ls=[]
# for i in range(len(l1)):
#     ls.append({l1[i]:{l2[i]:l3[i]}})
# print(ls)

# import colorama as c 
# print(c.Style.BRIGHT)
# print(c.Fore.RED,"Salom bolalar")
# print(c.Back.RED,"Hello")
# print(c.Style.RESET_ALL,"Tamom")


# try:
#     print(2/0)
# except:
#     print("No'lga bo'lish taqiqlanadi")
# print("salom")

# class Dog:
#     def __init__(self,nomi,yoshi,rangi):
#         self.name=nomi
#         self.age=yoshi
#         self.color=rangi
#     def show(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Color:",self.color)
# guffy=Dog("Guffy",5,":Brown")
# guffy.show()
# barbos=Dog("Barbos",2,"Black")
# barbos.show()


# INHERITANCE 

# class Human:
#     def __init__(self,a,b):
#         self.name=a
#         self.age=b
#     def __del__(self):
#         print("Object was destruction")
# ob1=Human("Abdull",29)
# print(ob1)
# del ob1
# print(ob1)

# class Direktor():
#     def __init__(self,ismi,oylik):
#         self.name=ismi
#         self.price=oylik
#     def show_info(self):
#         print(f"Name: {self.name}\nPrice: {self.price}")
# class Xodim(Direktor):
#     def __init__(self, ismi, oylik,lavozim):
#         super().__init__(ismi,oylik)
#         self.status=lavozim
#     def show_info(self):
#         super().show_info()
#         print(f"Status: {self.status}")
# boshliq=Direktor("Shuxrat",12000)
# boshliq.show_info()
# ishchi=Xodim("Davron",8000,"Injiner")
# ishchi.show_info()


# Inheritance turlari

# class A():
#     a=10
# class B(A):
#     b=20
# class C(B):
#     c=30
# class D(C):
#     d=40
# ob=D()
# print(ob.a,ob.b,ob.b,ob.c,ob.d)
    


# Encapsulation

# class Karta():
#     def __init__(self,nomi,raqami):
#         self.name=nomi
#         self.number=raqami
#         self.__code=1111
#     def info(self):
#         print("Card name:",self.name)
#         print("Card number:",self.number)
#         print("Card code:",self.__code)
#     def get_code(self):
#         return self.__code
#     def set_code(self,new_code):
#         self.__code=new_code
# uzcard=Karta("Asaka",3534652563555567345654)
# uzcard.info()
# uzcard.name="Aloqa"
# uzcard.number=3456356652342456426
# uzcard.set_code(5555)
# uzcard._Karta__code=7777
# uzcard.info()


# Polimorfism

# 1
# print(2+3)
# print("Salom"+ "bolalar")
# print(True+3.1415)
# print(2*3)
# print("salom"*3)

# 2
# print(len("salom"))
# print(len([1,2,3,4,5]))

# 3
# class Animal():
#     def __init__(self,nomi):
#         self.name=nomi
#     def voice(self):
#         pass
# class Dog(Animal):
#     def voice(self):
#         print("Wow wow woooow")
# class Cat(Animal):
#     def voice(self):
#         print("Myau myau myauuuu")
# Tomas=Cat("Thomas")
# Tomas.voice()
# Drooppy=Dog("Drooppy")
# Drooppy.voice()

# ABSTRACTION

# from abc import ABC,abstractclassmethod
# class Car(ABC):
#     @abstractclassmethod
#     def tezlik(self):
#         print("Abstract metod")
# class Tesla(Car):
#     def tezlik(self):
#         print("Tesla tezligi 400 km/soat")
# class Suzuki(Car):
#     def tezlik(self):
#         print("Suzuki tezligi 250 km/soat")
# class Jiguli(Car):
#     def tezlik(self):
#         pass
# ob=Jiguli()
# ob.tezlik()
# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday?"))
# if (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat>=30:
#     print("Cho'milgani ketdik!")
# elif (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat<30:
#     print("Uyda dam olamiz!")

# narh = 15000 # mijoz 15000 so'mga taom oldi.
# choy = False # mijoz choy ham oldi
# salat = False # mijoz salat olmadi

# if choy and salat: # agar mijoz choy ham salat ham olgan bo'lsa
#     narh = narh + 10000 # narhga 10000 so'm qo'shamiz
# elif choy or salat: # agar choy yoki salat olgan bo'lsa
#     narh = narh + 5000 # narhga 5000 so'm qo'shamiz
# else:
#     narh = narh + 0

# print(f"Jami {narh} so'm") # yakuniy narhni chiqaramiz

# narh = 15000 # mijoz 15 so'mga ovqat oldi
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False
# #Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
# if choy:   # agar choy olsa
#     print("Mijoz choy oldi.")
#     narh = narh + 3000
# if salat:  # agar salat olsa
#     print("Mijoz salat oldi.")
#     narh = narh + 5000
# if non:    # agar non olsa
#     print("Mijoz non oldi.")
#     narh = narh + 2000
# if kompot: # agar kompot olsa
#     print("Mijoz kompot oldi.")
#     narh = narh + 5000
# if assorti: # agar assorti olsa
#     print("Mijoz assorti oldi.")
#     narh = narh + 15000
    
# print(f"Jami {narh} so'm")

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# 'manti' in menu # menu da manti bormi?

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# ovqat = input('Nima ovqat yeysiz?>>>')
# if ovqat.lower() in menu:
#     print('Buyurtma qabul qilindi.')
# else:
#     print('Afsuski bizda bunday ovqat yo\'q')

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]

# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"Menuda {taom} bor")
#     else:
#         print(f"Kechirasiz, menuda {taom} yo'q")

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]

# if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Kechirasiz, menuda {taom} yo'q")
# else: # agar ro'yxat bo'sh bo'lsa
#     print("Savatchangiz bo'sh!")

# a=int(input("Juft son kiriting: "))
# if a%2==0:
#     print("Raxmat")
# else:
#     print("Bu son juft emas")


# a=int(input("Yoshingizni kiriting: "))
# if a<=4 or a>=60:
#     print("Siz uchun chipta bepul")
# elif a<=18 and a>4:
#     print("Siz uchun chipta narxi 10 000 so'm")
# else:
#     print("Siz uchun chipta narxi 20 000 so'm")

# a=int(input("Birinchi sonni kiriting: "))
# b=int(input("Ikkinchi sonni kiriting: "))
# if a<b:
#     print(f"{b} soni {a} sonidan katta")
# elif a>b:
#     print(f"{a} soni {b} sonidan katta")
# else:
#     print("Kiritilgan sonlar o'zaro teng ")

# mahsulotlar=['makaron','guruch',"yog'","yong'oq",'tamat','ketchup','bodring','sabzi','suv','olma']
# savat=[]
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qushing: "))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor! ")
#     else:
#         print(f"Do'konimizda {mahsulot} yo'q! ")


# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# if mavjud_emas:
#   print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
#   for mahsulot in mavjud_emas:
#     print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
    
    
