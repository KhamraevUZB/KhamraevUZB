'''a=int()
print(a,type(a))
a=123
print(a,type(a))
a=3.1415
print(a,type(a))
b=float()
print(b,type(b))
c=bool()
print(c,type(c))
c=True
print(c,type(c))'''




# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# print("Birinchi meva: ", mevalar[0].title())
# print("Ikkinchi meva: ", mevalar[2].upper())

# narhlar = [12000, 18000, 10900, 22000]
# print(narhlar[2] + narhlar[3])

# car_models = ['Toyota', 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Volkswagen']
# print(car_models[-6]) # Listning eng oxirgi elementiga -1 bilan murojat qilamiz 

# narhlar = [12000, 18000, 10900, 22000]
# narhlar[0] = 13000 # 1-qiymatni 13000 ga o'zgartiramiz
# narhlar[2] = 11000 # 3-qiymatni 11000 ga o'zgartiramiz
# narhlar[3] = narhlar[3]+2000 # 4-qiymatga 2000 qo'shamiz
# print(narhlar)

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# mevalar.append("tarvuz") # mevalar ga tarvuz qo'shamiz
# print(mevalar)

# cars = [] # bo'sh ro'yxat yaratamiz
# cars.append('Lacetti') # ro'yxatga Lacetti mashinasini qo'shamiz
# cars.append('Nexia 3') # ro'yxatga Nexia 3 mashinasini qo'shamiz
# cars.append('Cobalt')  # ro'yxatga Cobalt  mashinasini qo'shamiz
# print(cars)

# cars = ['Lacetti', 'Nexia 3', 'Cobalt']
# cars.insert(0, 'Malibu') # 1-o'ringa yangi qiymat qo'shamiz
# print(cars)

# cars.insert(2, 'Damas') # 3-o'ringa yangi qiymat qo'shamiz
# print(cars)

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
# del mevalar[1] # 2-element (anjir) ni o'chirib tashlaymiz
# print(mevalar)

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
# mevalar.remove('shaftoli') # Ro'yxatdan shaftolini o'chirdik
# print(mevalar)

# hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
# hayvonlar.remove("mushuk") # Ro'yxatda 2 ta mushuk bor, ulardan birinchisi o'chadi
# print(hayvonlar)

# bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
# mahsulot = bozorlik.pop(3) # Ro'yxatdan banan ni sug'urib olamiz
# print("Men " + mahsulot + " sotib oldim")
# print("Olinmagan mahsulotlar: ", bozorlik)

# ismlar=['Azamat','Islom','Bobur']
# dost=ismlar[0]
# dost2=ismlar[2]
# print("Salom " + ismlar[0] + ", bugun futbolga boramizmi?")
# print(dost2 + ", senchi borasanmi?")

# t_shaxslar=['Alisher Navoi','Amir Temur','Jaloliddin Manguberdi']
# z_shaxslar=['Ilon Musk','Bill Gets','Jim Kerry']
# zamonaviy=z_shaxslar[0]
# print("Men tarixdagi " + t_shaxslar.pop(1) + ", bilan gaplashishni xoxlagan bo'lar edim")
# print("Hozirgi zamondagi "+ zamonaviy+", bilan suxbat qurush orzuyim bor")

# friends=[]
# friends.append('Bobur')
# friends.append('Guli')
# friends.append('Temurbek')
# friends.append('Azamat')
# print(friends)
# friends.remove('Guli')
# print(friends)
# friends.insert(0,'Sardor')
# friends.append('Dilmurod')
# print(friends)
# mehmonlar=[]
# mehmonlar.append(friends.pop(3))
# mehmonlar.append(friends.pop(0))
# print("Mehmonga kelgan do'stlarim ", mehmonlar)


# LISTLAR BILAN ISHLASH

# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# print(cars)

# sonlar=[]
# for i in range(5,101,5):
#     sonlar.append(i)
# print(sonlar)
# print(max(sonlar))




# for i in range(1,10):
#     for j in range(1,10):
#         print(f"{i} * {j} = {i * j}")
#     print()


# LINEAR SEACHER
# BINARY SEACHER
# def linear_seach(list,item):
#     for n in range(len(list)):
#         if list[n]==item:
#             return n
#     return None

# def binary_seach(list,item):
#     low=0
#     high=len(list)-1
#     while low<=high:
#         mid=(low+high)//2
#         gues=list[mid]
#         if gues==item:
#             return mid
#         if gues>item:
#             high=mid-1
#         else:
#             low=mid+1
#     return None

# myList=[1,3,4,6,7,8,10,12,23,45,56,78,99]
# print(binary_seach(myList,10))
# print(linear_seach(myList,10))


# def linear_seach(list,item):
#     for n in range(len(list)):
#         if list[n]==item:
#             return n
#     return None

# def binary_seach(list,item):
#     low=0
#     high=len(list)-1
#     while low<=high:
#         mid=(low+high)//2
#         gues=list[mid]
#         if gues==item:
#             return mid
#         if gues>item:
#             high=mid-1
#         else:
#             low=mid+1
#     return None

# myList=range(1,1000)
# print(binary_seach(myList,10))
# print(linear_seach(myList,48))
# for i in myList:
#     if i%10==0:
#         print(i,end=' ')

# def is_prime(n):
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# # Foydalanuvchidan sonni kiritishni so'rash
# number = int(input("Sonni kiriting: "))

# # Tub yoki yo'qligini tekshirish
# if is_prime(number):
#     print(f"{number} tub son.")
# else:
#     print(f"{number} tub son emas.")


# import math
# for j in range(10, 1000):
#     prime = 1
#     for i in range(2, int(math.sqrt(j)) + 1):
#         if j % i == 0:
#             prime = 0
#             break
#     if prime == 1:
#         print(j)

# for i in range(1,100):
#     print(i,end=' ')


'''import turtle as T
import time

T.setup(1000,800,0,0)
T.speed(0)
T.penup()
T.seth(90)
T.fd(340)
T.seth(0)
T.pendown()
T.speed(5)
T.begin_fill()
T.fillcolor('red')
T.circle(50,30)

for i in range(10):
    T.fd(1)
    T.left(10)
T.circle(40,40)

for i in range(6):
    T.fd(1)
    T.left(3)
T.circle(80,40)

for i in range(20):
    T.fd(0.5)
    T.left(5)
T.circle(80,45)

for i in range(10):
    T.fd(2)
    T.left(1)
T.circle(80,25)

for i in range(20):
    T.fd(1)
    T.left(4)
T.circle(50,50)

time.sleep(0.1)

T.circle(120,55)
T.speed(0)
T.seth(-90)
T.fd(70)
T.right(150)
T.fd(20)
T.left(140)
T.circle(140,90)
T.left(30)
T.circle(160,100)
T.left(130)
T.fd(25)
T.penup()
T.right(150)
T.circle(40,80)
T.pendown()
T.left(115)
T.fd(60)
T.penup()
T.left(180)
T.fd(60)
T.pendown()
T.end_fill()
T.right(120)
T.circle(-50,50)
T.circle(-20,90)
T.speed(1)
T.fd(75)
T.speed(0)
T.circle(90,110)
T.penup()
T.left(162)
T.fd(185)
T.left(170)
T.pendown()
T.circle(200,10)
T.circle(100,40)
T.circle(-52,115)
T.left(20)
T.circle(100,20)
T.circle(300,20)
T.speed(1)
T.fd(250)
T.penup()
T.speed(0)
T.left(180)
T.fd(250)
T.circle(-300,7)
T.right(80)
T.circle(200,5)
T.pendown()
T.left(60)
T.begin_fill()
T.fillcolor('green')
T.circle(-80,100)
T.right(90)
T.fd(10)
T.left(20)
T.circle(-63,127)
T.end_fill()
T.penup()
T.left(50)
T.fd(20)
T.left(180)
T.pendown()
T.circle(200,25)
T.penup()
T.right(150)
T.fd(180)
T.right(40)
T.pendown()
T.begin_fill()
T.fillcolor('green')
T.circle(-100,80)
T.right(150)
T.fd(10)
T.left(60)
T.circle(-80,98)
T.end_fill()
T.penup()
T.left(60)
T.fd(13)
T.left(180)
T.pendown()
T.speed(1)
T.circle(-200,23)
T.exitonclick()


ism="Abdulloh"
yosh=25
print(ism)
print(yosh,type(yosh))
ism="Anvar"
print(ism)
raqam=int(input("raqamni kiriting: "))
print(raqam)
print(f"Salom mening ismim {ism} yoshim {yosh} da")'''


"""
Factorial of a positive integer -- https://en.wikipedia.org/wiki/Factorial
"""

def fact(n):
    if n<0 or n==1 or n==0:
        print("1")
    else:
        print(n*fact(n-1))
son=5
fact(son)