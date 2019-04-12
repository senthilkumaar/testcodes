l1=['a','b','c','d','e']
# l2=['1','2','3','4','5','6','7']
# d={}
# for i in range(len(l1)):
#     d[l1[i]]=l2[i]
#
# print(d)
#
# z=zip(l1,l2)
# d1=dict(z)
# print(d1)
#
#
# print ({l1[i]:l2[i] for i in range(len(l1))})
#
# print([l1[i]+l2[i] for i in range(len(l1))])
#
# l3=[1,2,[3,4,[7,8]],[5,6]]
# finallist=[]
# def listvalue(lst):
#     for i in range(len(lst)):
#         if type(lst[i])==list:
#             listvalue(lst[i])
#         else:
#             finallist.append(lst[i])
#             continue
#     return sorted(finallist)
#
# print(listvalue(l3))


# d = {'a': {'b': {'c': {'d': {'e': 'f'},'n':'d g f'}, 'k': 'g'}}}
# def dictvalue(dct):
#     for k,v in dct.items():
#         if type(v)==dict:
#             dictvalue(v)
#         else:
#             dct.pop(k)
#
#
#     return dct
#
# print(dictvalue(d))

#
import copy
e={'a': '1', 'e': '5', 'b': '2', 'c': '3', 'd': '4'}
x = copy.deepcopy(e)
for k,v in x.items():
    del x[k]

print(e)

print(list(e))
#
# for elements in l1:
#     print(elements)
#     l1.remove(map(elements))
#
# print(l1)



