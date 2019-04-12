# class TestMethod(object):
#     cls_var = 1
#     @classmethod
#     def class_method(cls):
#         cls.cls_var += 1
#         print (cls.cls_var)
#
#     @staticmethod
#     def static_method():
#         TestMethod.cls_var += 1
#         print (TestMethod.cls_var)
# #call each method from class itself.
# TestMethod.class_method()
# TestMethod.static_method()
#
# #construct instances
# testMethodInst1 = TestMethod()
# testMethodInst2 = TestMethod()
#
# #call each method from instances
# testMethodInst1.class_method()
# testMethodInst2.static_method()
# testMethodInst1.class_method()
# testMethodInst2.static_method()


# from array import *
# from numpy import *
# ar=array([1, 2, 3, 4, 5, 6])
# print(ar)
# a=zeros(5,int)
# print(a)

# s={}
# bandlist=[]
# band= input("enter the bands: ").split(',')
# bandlist.extend(band)
# s[102]=['Aravin','E01',1200]
# def updateprice(s):
#     if s[102][1] == 'E01':
#         s[102][2] = 1200
#     elif s[102][1] == 'E02':
#         s[102][2] = 1800
#     elif s[102][1] == 'E03':
#         s[102][2]==2400
# s[103]=['Aavin','E01',1200]
# print(s)
# s[102][1]='E02'
# updateprice(s)
# print(s[102])
# print(s[103])

str='$ymbol123Ss@'
#taking special char
character=[]
Uppercase=[]
lowercase=[]
numbers=[]
for char in str:
    if char in ['@','!','#','$','%','^','&','*','(',')']:
        character.append(char)
    elif char in ['1','2','3','4','5','6','7','8','9']:
        numbers.append(char)
    elif char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        Uppercase.append(char)
    else:
        lowercase.append(char)

print("special char: ",character)
print("Upper case:",Uppercase)
print("Lower case:",lowercase)
print("numbers: ", numbers)