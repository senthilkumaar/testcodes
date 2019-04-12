import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}
m=collections.ChainMap(a,b)
print(m.maps)


m['e']='F'
print(m.maps)


m1=m.new_child()
print(m1.maps)
#
print('***************')
print(m1.maps[-1])

# #
m1['e']='f'
print(m1.maps)
print(m1.parents)