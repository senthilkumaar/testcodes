# a=[10,2,3]
# b=[8,3,9,2,1,78,55]
# def addlist(list1,list2):
#     c = []
#     for i in range(len(list2)):
#         c.append(list1[i]+list2[i])
#     c.extend(list1[len(list2):])
#     return c
#
# if len(a)>len(b):
#     print(addlist(a,b))
# else:
#     print(addlist(b,a))
# finallist=[]
# for i in range(len(b)):
#     if i%2==0:
#         if b[i]%2==0:
#             finallist.append(b[i])
#     else:
#         if b[i]%2!=0:
#             finallist.append(b[i])
#
# print(finallist)

# ## print the even and odd nos based on even ,odd  index
# e=0
# o=1
#
# for item in b:
#     if item % 2 == 0:
#         finallist.insert(e,item)
#         e=e+2
#     else:
#         finallist.insert(o,item)
#         o=o+2
#
# print(finallist)



# lt = ['r', 'eee', 'p', 'l', 'a', 'c', 'eee', 'm', 'eee', 'n', 't']
# newlt = []
# for item in lt:
#     if item not in newlt:
#         newlt.append(item)
#         stri = ''.join(newlt)
#
#
# print(stri)

#
# values = input("enter the values : ")
# complist=values.split(',')
# print(type(values))
# print((complist))


##################################################


a = [1,2,3,[4,5,[6,7,[20,30], [40,60,[80]], 12, 'x'], 'a'], [{'u':24}, 'k'], 9, 8]


# def recursiuvve(listing, l):
#     for item in listing:
#         if type(item) == list:
#             recursiuvve(item, l)
#         else:
#             l.append(item)
#
#             continue
#
#     print(l)
#
# recursiuvve(a, [])

finalist = []
def recursiuvve(listing):

    for item in listing:

        if type(item) == list:
            recursiuvve(item)
        else:
            finalist.append(item)


    return finalist



print(recursiuvve(a))