from collections import defaultdict
# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# d = defaultdict(list)
# for k,v in s:
#     d[k].append(v)
#
# print(d.items())

value= 'yohohoohyohoyohooo'
d= defaultdict(int)
for k in value:
    d[k]+=1

print(d.items())





