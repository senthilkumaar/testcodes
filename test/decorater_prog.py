# import string
# # decorater
# def findingvalue(fun):
#     def innervalue(v):
#         return list(string.ascii_letters)[v]
#     return innervalue
#
# @findingvalue
# def retvalu(value):
#     return value
#
# print(retvalu(0))



def outer(fun):
    msg = 'hi'
    def inner(value):
        print(msg+str(value))
        return fun(value)
    return inner()


def disp(value):
    return value
disp=outer(disp)
disp(5)



