from collections import OrderedDict

o=OrderedDict()
o['a']=3
o['c']=1
o['b']=4

print(o)


o.move_to_end('c',last=False)

print(o)

print(o.popitem())
o['d']=5

print(o.popitem(last=False))
print(o)