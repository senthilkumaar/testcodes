from inheritance import *
#importing sys for adding new

import sys
sys.path.insert(0,r'C:\Users\senthilkumaar.s\PycharmProjects\New_pack')

import os

from New_pack.sum_custom import sum_c, herbivor
new_animal=scavengers(1,"domestic")
print(new_animal.type)

a=herbivor.diff_way(1,"asd")
print(sum_c(2,3))
print(a.printall())
print(a.type)

with open(r'C:\Users\senthilkumaar.s.HCLTECH\PycharmProjects\untitled\New_pack\test.txt',"r+") as f:
    li=f.readline()
    print(li)
    with open(r'C:\Users\senthilkumaar.s\PycharmProjects\untitled\New_pack\log.txt','a+') as rf:
        rf.write(li)



f=open("",'')
#file operation
f.close()




os.rename(r'C:\Users\senthilkumaar.s\PycharmProjects\untitled\New_pack\log.txt',r'C:\Users\senthilkumaar.s\PycharmProjects\untitled\New_pack\log_naveen.txt')
#os.remove(r"C:\Users\senthilkumaar.s\PycharmProjects\untitled\ads\__init__.py")
os.removedirs(r"C:\Users\senthilkumaar.s\PycharmProjects\untitled\ads")
if __name__=='__main__':
    pass