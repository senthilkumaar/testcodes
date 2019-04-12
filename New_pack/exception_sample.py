l1=[1,2,3,4,5]
try:
    print(l1[2])
    f=open("",'r')
except IOError as e:
    print(e)
# except Exception as e:
#     print (e)
else:
    print("executed only if ty is success")
finally:
    print("I am in finally")

# try:
#     name = input('entet the filename: ')
#     f = open(name , 'r')
# except IOError:
#     print('File not found:', name)
# else:
#     n=len(f.readline())
#     print (name, 'has ', n  ,'lines')
#     f.close()