from array import array

import collections
str ='hai hai hai meera!'
dict={}

for word in str.split():
    dict[word]=dict.get(word,0)+1
print(dict)



# for key,values in dict.items():
#     if values>0:
#         print(key,end='\t')


# l=[[1,2,3],[4,5,6],[7,8,9]]
#
#
#
#
# l1=[18,20,16,2,13,4]
# list=sorted(l1)
# print(list)
# def search(value):
#     for i in range(len (list)):
#         if  int(list[i])> value:
#             if i==0:
#                 return list[i]
#             else:
#                 return list[i-1]
#         else:
#             continue
#
# print(search(15))