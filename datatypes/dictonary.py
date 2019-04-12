l=[1,2,3,5,1,3]
# dict={}
# for x in l:
#     dict[x]=dict.get(x,0)+1
#
# print(dict)
#
#
l2=[1,2,3,4,5,6]
#
# c=[]
# for x in range(len(l)):
#     c.append(l[x]+l2[x])
#
# print(c)



d=dict(zip(l,l2))
for i in d.items():
    del i

print(d)
