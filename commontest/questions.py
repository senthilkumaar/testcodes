import string
person="Aran123"
nameList=list(person)
k=[]
j=[]
for item in person:
    if item in string.ascii_lowercase:
        k.append(item)
    else:
        j.append(item)

print(''.join(k))
print(''.join(j))
print(type(k))


###################list comprhension############################
# s= 'my name is senthil'
# print ([s[x] for x in range(0,len(s)) if (x%2!=0)])
#
#
# # print odd numbers
#
# print([x for x in range(0,100) if x%2 is not 0])

#######tuple comprehension ###############
#
# print({s:s for s in range (0,100)})



#/////////////class and static method////////######

#
# class person:
#     a=10
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     @classmethod
#     def dispname(cls,name,year,sex):
#         cls.sex=sex
#         return cls(name,(2018-year))
#
#     @staticmethod
#     def ageprint():
#         return person.a
#
# persondetail=person('naran',27)
# print(persondetail.name)
# p1=person.dispname('kave',1993,'male')
# print(p1.name)
# print(p1.sex)
# print(p1.age)
# print(person.ageprint())

########################

#
# tuples=([1,2,3,4,5],"welcome",12345)
# print(tuples)
#
# tuples[0].append(100)
# print(tuples[0])
# print(tuples)



