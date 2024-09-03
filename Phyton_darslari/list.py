#LIST 

# list2=[]
# list3=[123,3.145,'salom',True,False,2.73,'hayr']
# print(*list3)
# for i in list3:
#     print(i)
# list3.append(100)  #litni oxiriga 100 ni qoshadi
# list3.insert(2,'hello')   #listni 2 indexshiga helloni qoshadi
# list3.clear()  #listni tozalab tashlaydi butunlay
# list3.pop() #qoshilgan 100 ni uchiradi
# list3.pop(1)      # litning 1 chi elemementini uchiradi
# list3.remove(False)   #Faslseni uchiradi
# list3.count() #count hisoblab beradi
# print(list3)

# list1=[1,1,1,2,2,2,3,3,5,True,2,1,12,1]
# print(list1.count(1))       # nechta 1 borligini hisoblab beradi
# print(list1.index(2))       # 2 soni qaysi indexda ekanligini topib beradi
# list1.reverse()     # listni ichidagi indexlarni teskari qilib beradi
# print(list1)
# list1.sort()        #indexni o'sish tartibida saralab beradi
# list1.sort(reverse=True)        #indexni kamayish tartibida saralab beradi
# print(list1)  #sort funksiyasi str va int da birgalikda ishlamaydi

# list=['salom','hayr','kuku','bubu']
# list.sort()    #demak alfavit boyicha saralab beradi sort indexlarni
# print(list)


#TUBE BILAN ISHLASH

# list=[[1,2,3],[4,5,6],[7,8,9]]   #matrisa korinishida chiqadi
# for i in list:
#     print(*i)
# for i,j,k in list:
    # print(i,j,k)
    
# list1=[1,2,3,4,5]
# list2=[6,7,8,9,10]      # ikkalasini malumotlarini qoshyabdi
# print(list1+list2)      # 1,2,3,4,5,6,7,8,9,10


# a=12        #oddiy ozgaruvchini ozgartirsa boladi lekin listni uzgartirmaydi
# a=str(a)
# print(a,type(a))        #ozgaruvchini boshqa tipga ogirish


# t1=tuple()      # tuple o'zgarmas ma'lumot
# t2=()
# t3=(1,2,3,True,False,"salom",'hayr')
# print(t3,type(t3))
# print(t3[0])        #tuple ni 0 - elementini chiqarish
# print(t3.count(1))      # 1 necha marta ishlatilgani bilish
# print(t3.index(False))      #false nechanchi indexdaligini topish


#TUPLE VA LIST BILAN ISHLASH


