#closures

# x=5
# def outer():
#     x = 1
#     def inner():
#
#         print(x)
#         # 1
#         return x
#
#     return inner
#
#
# foo = outer()
# print(foo)
# print(foo())



for i in range(0,10):
    print(i)










'''
#decoratoe
def outer(some_func):
    def inner1():
        print ("before some_func")
        ret = some_func() # 1
        return ret + 1
    return inner1
@outer
def foo():
    return 1

#foo = outer(foo) # 2

print(foo())
'''


# def logger(fun):
#     def fun_log(*args):
#         print(fun(*args))
#     return fun_log
#
# def sum(a,b):
#     return a+b
#
# add_log=logger(sum)
# add_log(3,4)



def smart_divide(func):
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Whoops! cannot divide")

      return func(a,b)

   return inner

@smart_divide
def divide(a,b):
    return a/b


print(divide(6,3))
