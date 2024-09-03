# CLASS TUSHUNCHASI

# class Human:
#     name="Abdulla"
#     surname="Abdullayev"
#     age=20
#     def run(self):
#         print(self.name,"is running in the park")
#     def bark(self):
#         print("Aaaaaaaaaaaaaaaaa")
# odam1=Human()
# print(odam1.surname,odam1.name,odam1.age)
# odam1.run()
# odam1.bark()

# class Dog:
#     def __init__(self,nomi, yoshi,rangi):
#         self.name=nomi
#         self.age=yoshi
#         self.color=rangi
#     def show(self):
#         print(self.name)
#         print(self.age)
#         print(self.color)
# guffy=Dog("Guffy",5,"Brown")
# guffy.show()
# barbos=Dog("Barbos",6,"Qora")
# barbos.show()


# INHERITANCE

# class Human:
#     def __init__(self,a,b):
#         self.name=a
#         self.age=b
#     def __del__(self):
#         print("Object was destruction")
# ob1=Human("Abdulla",20)
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
#     def __init__(self, ismi, oylik, lavozim):
#         super().__init__(ismi, oylik)
#         self.status=lavozim
#     def show_info(self):
#         super().show_info()
#         print(f"Status: {self.status}")
# boshliq=Direktor("Shuxrat",12000)
# boshliq.show_info()
# ishchi=Xodim("Davron",8000,"Injiner")
# ishchi.show_info() 



# class Direktor():
#     def __init__(self,lavozim, ism, familya,oylik):
#         self.status=lavozim
#         self.name=ism
#         self.surname=familya
#         self.price=oylik
#     def show(self):
#         print(f"Lavozim: {self.status}\nIsm: {self.name}\nFamilya: {self.surname}\nOylik: {self.price}")
        
# class Genditektor():
#     def __init__(self,muddat, opit, reyting):
#         self.vaqt=muddat
#         self.opit=opit
#         self.reyt=reyting
#     def info(self):
#         print(f"Ishlash yili: {self.vaqt}\nMalaka: {self.opit}\nReyting: {self.reyt}")
        
# class Xodim(Direktor,Genditektor):
#     def __init__(self, lavozim, ism, familya, oylik,yoshi,vaqt,opit,reyt):
#         Direktor.__init__(self,lavozim, ism, familya, oylik)
#         Genditektor.__init__(self,vaqt,opit,reyt)
#         self.age=yoshi
#     def show(self):
#         super().show()
#         print(f"Yosh: {self.age}")

# ishchi=Xodim("Qorovul","Behzod","Lapasov",1200000,43,5,10,5)
# ishchi.show()
# ishchi.info()



# class Dog:
#     name="Guffy"
#     age=12
#     def info(self):
#         print(self.name, "juda tez yuguradi")
#     def info1(self):
#         print("va uning yoshi", self.age, "da")
# kuchuk=Dog()
# kuchuk.info()
# kuchuk.info1()
        
        
# INHERITANCE TURLARI

# class A():
#     def show(self):
#         print("Hello")
# class B(A):
#     def hide(self):
#         print("Goodbye")
# ob=B()
# ob.show()
# ob.hide()
# n=A()
# n.show()



# class A():
#     a=10
# class B(A):
#     b=20
# class C(B):
#     c=30
# i=B()
# print(i.a, i.b)
# j=C()
# print(j.a, j.b, j.c)

# class A():
#     a=10
# class B():
#     b=20
# class C(A,B):
#     c=30
# i=C()
# print(i.a, i.b, i.c)


# ENCAPSULATION


# class Karta():
#     def __init__(self,nomi, raqami):
#         self.name=nomi      #public
#         self.number=raqami  #public
#         self.__code=1111    #private yani yopiq
#     def info(self):
#         print("Card name: ", self.name)
#         print("Card number: ", self.number)
#         print("Card Code", self.__code)
#     def get_code(self):
#         return self.__code
#     def set_code(self,new_code):
#         self.__code=new_code
# uzcard=Karta("Asaka",12345678901234)
# uzcard.info()
# uzcard.name="Xalq Banki"
# uzcard.number=19876543210987
# uzcard.set_code(4444)
# uzcard.info()
# uzcard._Karta__code=7777
# uzcard.info()


# class Karta():
#     def __init__(self,nomi, raqami):
#         self.name=nomi      #public
#         self.number=raqami  #public
#         self.__code=1111    #private yani yopiq
#     def info(self):
#         print("Card name: ", self.name)
#         print("Card number: ", self.number)
#         print("Card Code", self.__code)
#     def get_code(self):
#         return self.__code
#     def set_code(self, new_code):
#         self.__code=new_code
# uzcard=Karta("Asaka",12345678901234)
# uzcard.info()
# uzcard.name="Xalq Banki"
# uzcard.number=19876543210987
# uzcard.set_code(5555)
# uzcard.info()
# uzcard.get_code()



# POLIMORFISM

# class Animal():
#     def __init__(self,nomi):
#         self.name=nomi
#     def voice(self):
#         pass
# class Dog(Animal):
#     def voice(self):
#         print("Wow Wow Woooow")
# class Cat(Animal):
#     def voice(self):
#         print("Myau miau miau")
# Tomas=Cat("Thomas")
# Tomas.voice()
# Drooppy=Dog("Drooppy")
# Drooppy.voice()


# ABSTRACTION


