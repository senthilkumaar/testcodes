


# d = {'a': {'b': {'c': {'d': {'e': 'f'},'n':'d g f'}, 'k': 'g'}}}

d = {'a': {'b': {'c': {'d': {'e': 'f'}}, 'fj': {'z': 'x y q'}}}, 'k': 'g'}
# d={'a':{'b':{'c':{'d':{'e':'f'}}}},'k':'g'}

# d={'a': {1: {1: 2, 3: 4}, 2: {5: 6}}}
def recursive(d):
    for key, value in d.items():
        print(key)
        if type(value)== dict:
            recursive(value)
        else:
            continue
            # print(value)

recursive(d)


# dict process

#
# if hash(1)==hash(1.0002):
#     print (True)
# else:
#     print(False)
# print(hash(1),hash(1.0002))




# def argts(a,**kwargs):
#     print(a)
#     for item in kwargs:
#         print('args', item)
#
#
# argts(5,c= 3)