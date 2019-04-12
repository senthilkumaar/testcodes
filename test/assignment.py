#1	Write a python program using while loop that will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# x=2000
# while (x<3201):
#     if x%7 == 0 and x%5 != 0:
#         print(x)
#         x=x+1
#     else:
#         x=x+1

####################################################################################

#Write a python program using for loop & function to find factorial of a given numbers

# def factoriral(num):
#     n = 1
#     for i in range(1,num+1):
#         n = n*i
#     print(n)
#
# num = int(input("enter the no: "))
# factoriral(num)


#####################################################################################

#Write a python program using function to search for an element stored in Dictionary
d={'a':1, 'b':2, 'c':3 }

def searchingdict(ele):
    if ele in d:
        print(ele)
        print(d[ele])
    else:
        print(ele)
        print(" no such element in dict exists")

ele=input("enter the element to search: ")
searchingdict(ele)

#####################################################################################
#
# Write a python program Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98') and other operation like searching the list & tuple for particular number.

# values = input("enter the values : ")
# complist=values.split(',')
# comptup= tuple(complist)
# print(complist)
# print(comptup)
#
# val = input("enter the element to search : \n")
#
#
#
# def searchlt(val):
#     if val in complist:
#         print("value {} exists in list at index :{}".format( val, complist.index(val)))
#
#     else:
#         print("no such value")
#
#
# def searchtp(val):
#     if val in comptup:
#         print("value {} exists in tuple at index :{}".format(val, comptup.index(val)))
#     else:
#         print("no such value")
#
#
#
# searchlt(val)
# searchtp(val)

#####################################################################################

#Write a python program to find Fibonacci series of a given number using if-else.

# num = int(input("enter the no to find the fibonacci series: "))
#
# def Fibonacci(n):
#     if n<0:
#         print("Incorrect input")
#
#     elif n==1:
#         return 0
#
#     elif n==2:
#         return 1
#     else:
#         return Fibonacci(n-1)+Fibonacci(n-2)
#
# value=Fibonacci(num)
# print(value)


#####################################################################################

#Write a small program implementing Lambda

# from functools import reduce
# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
#
# f = list(filter(lambda x: x%2==0 ,li))
# print(f)
#
# m = list(map(lambda x: x*x,li))
# print(m)
#
# r = reduce(lambda x,y: x + y,li)
# print(r)

###################################################################################

#Write a python program that gets a string as input &
#  do the following actions on that string like:
#  slitting a string if whitespace found & print them,
#  find length of string, uppercase to lowercase, sorting

#
# s = 'Welcome to the jungle'
#
# print(s.split(" "))
# print("length of the string: ",len(s))
# print(s.upper())
# print(s.lower())
# print(sorted(s))

###################################################################################

#Write a python program that implements all file operations like opening, reading,
# writing, closing, appending etc.

# writing
# with open (r'C:\Users\senthilkumaar.s.HCLTECH\Desktop\testscript.txt','w+') as f:
#     f.write("welcome to the python script")
#     f.close()
#

# reading and appending
#
# with open (r'C:\Users\senthilkumaar.s.HCLTECH\Desktop\testscript.txt','r+') as g:
#
#     g.write(" add to the next level")
#     print(g.read())
#     g.tell()
#     g.close()


###################################################################################

#Write a python program that implements module.
#
# from math import sin
#
# num = int(input("enter the sin value: "))
# print(sin(num))

###################################################################################
#Write a python program implementing seek in file.
# with open (r'C:\Users\senthilkumaar.s.HCLTECH\Desktop\testscript.txt','r+') as g:
#     g.seek(0)
#
#     g.write(" add to the first now ")
#     g.close()