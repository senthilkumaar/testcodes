def test_lambda(x,y):
    return x+y

print(test_lambda(3,5))
f=lambda x,y : x+y
print(f(2,5))

l1=[x for x in range(0,20)]

print (l1)
import functools
l2=map(lambda x:x/2,l1)
l3=functools.reduce(lambda x,y:x+y,l1)
print(list(l2))
print(l3)


l4=[[1 for x in range(3)] for y in range(3)]

print (l4)