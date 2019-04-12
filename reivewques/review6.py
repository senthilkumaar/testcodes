# class a:
#     def m(self):
#         print("A")
# class b:
#     def m(self):
#         print("B")
#
# class d(a):
#     def m(self):
#         print("D")
#
#
# class c(d,a):
#     def m(self):
#         a.m(self)
#         print(super())
#         super().m()
#         print("C")
#
# class e(c,d):
#     def m(self):
#         d.m(self)
#         print(super())
#         super().m()
#         print("e")
#
# cobj=e()
# cobj.m()

#setattr(c, 'v', "Naveen")          # dynamic allocation

#print(cobj.v)

'''
i_str="aaabcddee"
print({x:(i_str.count(x)) for x in set(i_str)})
'''

#
d={'a':{'b':{'c':{'d':{'e':'f'}}},'k':'g'}}

#print([x for x in str(d) if x.isalpha()])

# def recursive_fetch(d):
#     k=list(d.keys())[0]
#     if d[k]!=str:  # exit condition in recursive condition .
#         key_0=list(d.keys())[0]
#         print(key_0,end=' ')
#         recursive_fetch(d[key_0])
#     else:
#         print(d.values())
#
# recursive_fetch(d)
#

def recursive_items(d):
    for key,value in d.items():
        if type(value) is dict:
            yield (key)
            yield from recursive_items(value)
        else:
            yield (value)

# a = {'a': {1: {1: 2, 3: 4}, 2: {5: 6}}}

for key in recursive_items(d):
    print(key)


#i="aaabccdee"

'''
print (set(i))
for h in [(x,i.count(x)) for x in set(i)]:
    print(str(h[0])+''+str(h[1]),end='')
##############
count=0
result=""
for x in range(1,len(i)):
    if(i[x-1]==i[x]):
        count+=1
    else:
        if(count!=0):
            result+=str(count+1)
            count=0
            result+=i[x-1]
    if(count!=0):
        result+=str(count+1)
        count=0
    result+=i[x-1]
print (result)
'''

# for ele in range(0,len(i)):
#     if (i[ele-1] != i[ele]):
#             counting=i.count(i[ele])
#             print("{}{}".format(i[ele],counting),end="")

### faulty one in hand

#
# i="aaabccdee"
# count = 0
# for ele in range(0,len(i)-1):
#
#     if i[ele]==i[ele+1] or i[ele]==i[ele-1]:
#
#         count=count +1
#
#     elif i[ele]!=i[ele+1]:
#         count=0
#         count = count + 1
#     else:
#         continue
#
#
#     print('{0} {1}'.format(i[ele], count))

# i="aaabccdeecccaaabbbbnnnmm"
#
# count=0
# result=""
# for x in range(1,len(i)):
#     if(i[x-1]==i[x]):
#         count+=1
#     else:
#         if(count!=0):
#             result+=str(count+1)
#         count=0
#         result+=i[x-1]
# if(count!=0):
#     result+=str(count+1)
# count=0
# result+=i[x-1]
# print (result)

