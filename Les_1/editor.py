'''das 1'''
# a=5
# b=4
# c=(a**2+b**2)**0.5
# print(c)
# print(type(c))
#
# name="Rafo"
# name.upper()
# print(name)

# a=int(input("koxm"))
# s=a**2
# # print(s)
# import random


'''legal popoxakaner'''
# myvar = "Armen"
# my_var = "Armen"
# _my_var = "Armen"
# myVar = "Armen"
# MYVAR = "Armen"
# myvar2 = "Armen"


'''stugel tesaky'''
# x = 5
# y = "John"
# z=3.4
# print(type(x))
# print(type(y))
# print(type(z))


# a=int(input("koxm"))
# s=a**2
# print(s)


'''das 2, matematikakan operator'''
# x=8
# y=4
# print(x+y)
# print(x-y)
# print(x/y)
# print(x*y)

'''#mnacord'''
# x=8
# y=3
# print(x%y)


'''qani hat 3 ka 10i mej'''
# x=10
# y=3
# print(x//y)


'''astican bardzracnel'''
# x=4
# y=3
# print(x**y)


# balance=100
# paycheck=150
# print(balance+paycheck)


'''ture && false'''
# x=5
# y=4
# print(x>y)
# print(x==y)
# print(x!=y)
# print(x<=y)


# balance=100
# plus=150
# balance+=3*plus
# print(balance)

# balance=100
# x=float(input("avelacnel"))
# y=float(input("avelacnel"))
# z=float(input("avelacnel"))
# print(balance+x+y+z)


# x=3
# y=3
# if x>y:
#     print("x>y")
# elif x==y:
#     print("dzmbo")
# else:
#     print("yes")

'''tnayin'''
# x="py"
# y="thon"
# print(4*x+y)


# x="7p"
# y="79"
# print(3*x+y)


# pox=float(input("mutqagrel gumary"))
# yndanur=380000
# if pox>yndanur:
#     print("hajox")
# else:
#     for x in 20000,10000,5000,2000,1000:
#         while pox>=x:
#             pox-=x
#             print(x)


"""das 4"""

# x=float(input())
# print(x*60)


# x=str(input("uzum es sksel xaxy"))
# points=0
# if x=="ayo":
#  a=float(input("4+4"))
#  if a==8:
#   points+=1
#  b=float(input("2+3"))
#  if b==5:
#   points+=1
#   print(points)
# else:
#  print("hajox")


# anuns = ["Arman", "Jiro", "Goqor", "Valod"]
# for anun in anuns:
#     if anun == "Valod":
#         continue
#     print(anun)



'''das 5 '''

# import math
# print(math.pi)
# print(math.sqrt(16))
# print(math.sqrt(625))



# from math import *
# print(pi)


# import math as m
# print(m.pi)


# import random
# print(random.random())
#
# print(random.randint(1,10))

# x="abcfdeyz"
# print(random.choice(x))


# import random as r
# print(r.randrange(0,100,5))




# import time
# time.sleep(3)
# print("tes")

# import os
# print(os.getcwd())



# import calendar
# y=int(input("input the year"))
# m=int(input("input the month"))
# print(calendar.month(y,m))


#
# import datetime
# x=datetime.datetime.now()
# print(x)
# print(datetime.date.today())


#
# import datetime
# x=datetime.datetime(2021,8,1)
# print(x)


# import datetime
# x=datetime.datetime.now()
# print(x.year)
# print(x.strftime("%A"))



# import random
# x=float(input("grel tiv 1-10:"))
# y=random.randint(1,10)
# if x==y:
#     print("true")
# else:
#     print("false")



# import random
# x=float(input("grel tiv 1-10:"))
# y=random.randint(1,10)
# print(x==y)


# import random
# x=float(input("grel tiv 10-100:"))
# y=random.randint(10,100)
# print(x>y)

# import math
# a=6
# b=10
# c=1
# res=10**2-4*6*(-1)
# x1=(-10-(math.sqrt(res))/2*6)








'''fileri het ahsxatanq'''
# myFile=open("text.txt","r")
# print(myFile.readline())
# myFile.close()
'''with ovy miangamic pakuma fily el close petq chi'''
# with open("text.txt","r") as t:
#     print(t.readline())
'''cikl fral sax annunery hertov beruma'''
# with open("text.txt","r") as t:
#     for line in t.readlines():
#         print(line)
'''mer uzac toxov'''
# with open("text.txt","r") as t:
#     for line in t.readlines()[1:]:
#         print(line)

'''pythonic qcuma output txt i mej'''
# with open("output.txt","a") as f:
#     f.write("\n out new line")
'''w ovy jnjuma'''
# with open("output.txt","w") as f:
#     f.write("Deleted all lines")
'''taza file a bacum qo uzac anunov u qo uzac textov,ete 2angam run tanq errora talu'''
# with open("newFile.txt","x") as n:
#     n.write("barev cay")
'''mer uzac indexi tak gtnvox arjeqy konkret sranov azganunnery'''
# with open("text.txt","r") as t:
#     for line in t.readlines()[1:]:
#         print(line.split(",")[1])
'''asuma te vor toxuma axjik vorum txa'''
# with open("text.txt","r") as r:
#     for line in r.readlines()[1:]:
#         info=line[:-1].split(",")
#         if info[3]=="female":
#             print("axjik")
#         elif info[3]=="male":
#             print("txa")
#         else:
#             print("unkhnown")





'''das 6'''
'''amen tiv u tar uni ira id'''
# x=5
# print(id(x))




# x=str(input("greq bar-"))
# y=str(input("greq bar-"))
# print('a' in x)
# print('a' in y)




# x="banan,,tandz,xndzor,yelak"
# print("banan")
# print("banan" in x)
# print("orange")
# print("orange" in x)




# x=float(input("tiv-"))
# print(x>=-8 or x<12)
# print(x>=10 or x<=12)
# print(x%10==0 or x%10==1)
# print(x<4 or x>=50)


# x=float(input("tiv-"))
# print(x>9 and x<50)
# print(x<=1 and x>11)
# print(x//10==3 and x%10==1)
# print(x//3==0 and x>=17)





# import random
#
# a = "light on", "light off"
# if random.choice(a) == "light on":
#     print("light on")
#     sarnaran = "lime,bananas,kiwi,grapefruit,mango,apples,avocado,apricots,guava,lemon"
#     x = "bananas" in sarnaran
#     y = "oranges" in sarnaran
#     z = "apples" in sarnaran
#     print(sarnaran)
#     print("bananas", x)
#     print("oranges", y)
#     print("apples", z)
#     if x == False:
#         print("go and buy bananas")
#     elif y == False:
#         print("go and buy oranges")
#     elif z == False:
#         print("Go and buy apples")
# else:
#     print("light off haneq uteliqnery")



'''loop for,range and while '''
# name=["Arm","Gag","Miqo"]
# for i in name:
#     print(i)

# name = "Arm"
# for i in name:
#     print(i)

'''range'''
# for i in range(6):
#     print(i)


'''while'''
# i=1
# while i<6:
#     print(i)
#     i+=1


# i=1
# while i<6:
#     print(i)
#     i+=1
#     if i==3:
#         break

'''zip'''
# list1=['Ani','Anna']
# list2=['Raf',"Gev"]
# for x,y in zip(list1,list2):
#     print(x,y)


# x=0
# while x<20:
#     x+=1
#     if x==11:
#         break;
#     print(x)

# import random
# point1=0
# point2=0
# me=str(input('dzer nshany-'))
# comp=['mkrat','qar','tuxt']
#     if me==random.choice(comp):
#         print("voch voqi")
#     if random.choice(comp)=='mkrat' and me=='tuxt':
#         print('comp win')
#         point1+=1
#     if random.choice(comp) == 'qar' and me == 'mkrat':
#         print('comp win')
#         point1 += 1
#     if random.choice(comp) == 'tuxt' and me == 'qar':
#       print('comp win')
#        point1 += 1
#     if random.choice(comp) == 'mkrat' and me == 'qar':
#         print('you win')
#         point2 += 1
#     if random.choice(comp) == 'qar' and me == 'tuxt':
#         print('you win')
#         point2 += 1
#     if random.choice(comp) == 'tuxt' and me == 'mkrat':
#         print('you win')
#         point2 += 1
#         while point1 < 4 or while point2 < 4:
#
#
#
# print(point1,point2)



'''das 8'''
# x=[11,34,56,45,67]
# print(min(x))



# zuyg=0
# kent=0
# x=0
# while x<100:
#     x+=1
#     if x%2==0:
#         print(x,"zuyg")
#         zuyg+=1
#     else:
#         kent+=1
#         print(x,"kent")
#
# print(zuyg,"hat zuyg,",kent,"hat kent")


'''fibonacci'''
# x,y=0,1
# while y<50:
#     print(y)
#     x,y=y,x+y
# tar=0
# tiv=0
# strin='python 3.9'
# for x in strin:
#     if x.isdigit():
#         tiv+=1
#     elif x.isalpha():
#         tar+=1
# print(tiv,"tiv",tar,"tar")

# y=0
# x=input("grel tiv-")
# for i in x:
#     z=int(i)
#     y+=z
# print(y)



'''das 9,10'''

'''()-tuple'''
'''{}-dictionary'''
'''[]-list'''


'''dictionary:key u value'''
# thisdict={"name":"Aram","year":1994}
# print(thisdict)

'''ete uzument popoxenq ajeqy'''
# thisdict={"name":"Aram","year":1994}
# thisdict["year"]=2014
# print(thisdict)

'''len() sra erkarutyuny 2'''
# thisdict={"name":"Aram","year":1994}
# print(len(thisdict))

'''add item'''
# thisdict={"name":"Aram","year":1994}
# thisdict["age"]=26
# print(thisdict)

'''del item'''
# thisdict={"name":"Aram","year":1994}
# del thisdict["year"]
# print(thisdict)

'''clear'''
# thisdict={"name":"Aram","year":1994}
# thisdict.clear()
# print(thisdict)





'''set frozenset (hamarvuma data type)'''
# set1={12,23,"11","hello"}
# print(set1)

'''set y random a inqy indexov chi jogum random tpuma'''
# this_set={'apple','banana','cherry'}
# for x in this_set:
#     print(x)

'''true'''
# this_set={'apple','banana','cherry'}
# print('banana' in this_set)
'''false'''
# this_set={'apple','banana','cherry'}
# print('banana' is this_set)

'''union() method hamematuma irar het krknvoxy hanuma u sax tpuma'''
# set1={'a','b','c'}
# set2={1,'a',3}
# set3=set1.union(set2)
# print(set3)

'''isthisjoint() hamematuma ete erkusne chi krknvum true a tali'''
# set1={12,23,'11','hello'}
# set2={14,3,'141','world'}
# print(set1.isdisjoint(set2))

'''exersices'''
# list={
#     'Aram':5,
#     'Gor':4,
#     'Andrey':6,
#     'Rafo':8,
#     'Hamo':7}
# print(list)

'''mijin tvabanakany'''
# list={'Aram':5,'Gor':4,'Andrey':6,'Rafo':8,'Hamo':7}
# x=list.values()
# res=0
# for i in x:
#     res+=i
# print(res/len(x))

'''milioner 5 harc amen harc 500 dram'''
# count=0
# while True:
#     harc1=input("vor tvina exel aprilyany? \n a)2016, b)1998 ,c)2012, d)2020--").upper()=="A"
#     if harc1 is True:
#         count+=500
#         print(count)
#     else:
#         print("You louse")
#         break
#     harc2 = input("Hayastani mayraqaxaqy? \n a)Moskva, b)Erevan ,c)Kiev, d)Tehran--").upper() == "B"
#     if harc2 is True:
#         count += 1000
#         print(count)
#     else:
#         print("You louse")
#         break
#     harc3 = input("ova grel hayoc aybubeny? \n a)Tumanyan, b)Isahakyan,c)Saryan, d)Mashtoc").upper() == "D"
#     if harc3 is True:
#         count += 2000
#         print(count)
#     else:
#         print("You louse")
#         break
#     x=str(input("cankanum eq sharunakel xaxy?--"))
#     if x=="ayo":
#         harc4 = input("Rusastani mayraqaxaqy? \n a)Erevan, b)Kiev ,c)Moskva, d)Vladivastok").upper() == "C"
#         if harc4 is True:
#             count += 4000
#             print(count)
#         else:
#             print("You louse")
#             break
#         print("duq vastakel eq",count,"dram")
#     break


'''ex1'''
# dict={"name":"Aram","year":1994}
# x=dict.values()
# print(x)

'''ex2'''
# dict={"mark":"BMW","year":2019}
# dict["color"]="black"
# print(dict)

'''ex3'''
# dict={"mark":"BMW","year":2019,"color":"black","model":"BMW"}
# print("color" in dict)

'''ex4'''
# dict1 = {'a': 50, 'b': 700}
# dict2 = {'c': 400, 'd': 600}
# x = dict1.copy()
# x.update(dict2)
# print(x)

'''ex5'''
# cucak={'Aram':5,'Gor':4,'Andrey':6,'Rafo':8,'Hamo':7}
# x=cucak.values()
# arjeq=1
# for i in x:
#     arjeq=arjeq*i
# print(arjeq)

'''ex6'''
# dict={'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# x=dict.values()
# print(max(dict),":",max(x))


'''les18 ex'''
# cucak={"Artak":"good","Hayk":"good","Roman":"bad","Narek":"bad"}
# print(cucak)

''''''
# cucak={"Artak":4,"Hayk":5,"Roman":10,"Narek":3,"Anahit":9}
# mark=cucak.values()
# for i in mark:
#     if i >= 5:
#         print(i)

''''''
# cucak={"Artak":4,"Hayk":5,"Roman":10,"Narek":3,"Anahit":9}
# mark=cucak.values()
# for i in mark:
#     if i < 5:
#         print(i)

''''''
# cucak= {"Artak":4,"Hayk":5,"Roman":10,"Narek":3,"Anahit":9}
# x =input("name--")
# print(cucak.get(x))

''''''
# list1 =[{'key1':'value1'},{},{},{'key1':'value1'},{'key2':'value2'}]
# res = []
# for i in list1:
#     if i not in res:
#         res.append(i)
# print(res)


'''ex3'''
# set={10,20,"hello"}
# set.add("Python")
# print(set)
'''ex4'''
# set={10,20,"hello","Python"}
# set.remove("Python")
# print(set)
'''ex6'''
# set1={'Hayk','Hakob','Aro'}
# set2={"Samo","Hayk","Rafo"}
# set3=set1.intersection(set2)
# print(set3)
'''ex7'''
# set1={'a','b','c'}
# set2={1,2,3,'c'}
# set3=set1.union(set2)
# print(set3)
'''ex8 ?????'''
# set1={'a','b','c'}
# set2={'a','b','c'}
# set3=set1.issuperset(set2)
# print(set3)

# set1={'a','b','c'}
# set2={'a','z','c'}
# set3=set1.issubset(set2)
# print(set3)
'''ex9'''
# set={'a','b','c'}
# set.clear()
# print(set)
'''ex10'''
# set={10,20,30}
# print(min(set))
# print(max(set))
'''ex11'''
# set={'a','b','c',1,2,3,"hi","python",("bye",3,4)}
# print(len(set))




'''das 11'''


