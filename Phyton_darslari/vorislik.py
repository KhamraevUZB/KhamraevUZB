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




class Direktor():
    def __init__(self, lavozim, ism, familya, oylik):
        self.status = lavozim
        self.name = ism
        self.surname = familya
        self.price = oylik

    def show(self):
        print(f"Lavozim: {self.status}\nIsm: {self.name}\nFamilya: {self.surname}\nOylik: {self.price}")

class Genditektor():
    def __init__(self, muddat, opit, reyting):
        self.vaqt = muddat
        self.opit = opit
        self.reyt = reyting

    def info(self):
        print(f"Ishlash yili: {self.vaqt}\nMalaka: {self.opit}\nReyting: {self.reyt}")

class Xodim(Direktor, Genditektor):
    def __init__(self, lavozim, ism, familya, oylik, yoshi, vaqt, opit, reyt):
        Direktor.__init__(self, lavozim, ism, familya, oylik)
        Genditektor.__init__(self, vaqt, opit, reyt)
        self.age = yoshi

    def show(self):
        super().show()
        print(f"Yosh: {self.age}")

# Foydalanuvchi kiritishlari
lavozim = input("Lavozimni kiriting: ")
ism = input("Ismni kiriting: ")
familya = input("Familyani kiriting: ")
oylik = int(input("Oylikni kiriting: "))
yoshi = int(input("Yoshini kiriting: "))
vaqt = int(input("Ishlash yilini kiriting: "))
opit = int(input("Malaka darajasini kiriting: "))
reyt = int(input("Reytingni kiriting: "))

# Xodim ob'ektini yaratish
ishchi = Xodim(lavozim, ism, familya, oylik, yoshi, vaqt, opit, reyt)

# Ma'lumotlarni ko'rsatish
ishchi.show()
ishchi.info()
