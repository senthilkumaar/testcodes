# str0 = 'Hello World!'
#
# str1='123456789'
# print(type(str1))
# print(int(str1))
# #finallist=list(map(str0,str1))
# d={str0:str1}
# print(d)
# l1=list(str0)
# l2=list(str1)
# print(l1,l2)
# f=zip(l1,l2)
# print(f)
# h=dict(f)
# print(h)
# print(tuple(str0))
# print(set(str0))
# i=10
# print (eval('i+10'))
# print(chr(97))
#


string = '''You are advised to take references of these examples and try them on your own.
All programs in this page are tested and should work on almost all Python3 compilers.
Feel free to use the source code on your system.'''
strr=string.split()
print(string.replace(" ",""))

# from collections import Counter
# str = "collections"
#
# def Printvalue(str):
#     listing = []
#     spattern = Counter(str)
#     for char in str:
#         chars = char * spattern[char]
#         if chars not in listing:
#             listing.append(chars)
#             finaloutput = ''.join(listing)
#         else:
#             continue
#
#     print(finaloutput)
#
#
# Printvalue(str)