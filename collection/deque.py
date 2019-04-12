from collections import deque

d=deque('Welcome to the jungle')



print('********************')
print(d)

d.append(5)


print('********************')
print(d)


d.appendleft(5)


print('********************')
print(d)
d.clear()

print('********************')
print(d)


d.extendleft('hai')



print('********************')
print(d)

d=deque('Welcome to the jungle')

d.pop()
d.popleft()
print('********************')
print(d)
print(list(reversed(d)))

d.extend('lk')
d.extendleft('kk')

print('********************')
print(d)
d.rotate(1)
print(d.rotate(1))
print(d.rotate(-1))

