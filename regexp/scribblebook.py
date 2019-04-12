# class test(object):
#     c=0
#     def value(self,a,b):
#         self.a=a
#         self.b=b
#         self.c=a+b
#         print(self.c)
#     @classmethod
#     def meth(cls):
#         print(cls.c)
#
# t=test()
# t.value(5,6)
# test.meth()
import collections
import random

# Set the random seed so we see the same output each time
# the script is run.
random.seed(1)

d1 = collections.deque(maxlen=3)
d2 = collections.deque(maxlen=3)

for i in range(6):
    n = random.randint(0, 100)
    print('n =', n)
    d1.append(n)
    d2.appendleft(n)
    print('D1:', d1)
    print('D2:', d2)