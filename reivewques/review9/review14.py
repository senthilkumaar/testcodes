# def get_data(item,listy = []):
#     listy.append(item)
#     return listy
#
#
# list1 = get_data(1, [2, 3])
# list2 = get_data(4)
# list3 = get_data(6, [7])
#
# print(list1)
# print(list2)
# print(list3)



class test(object):
    def __init__(self,name,age):
        assert (type(name)==str and type(age)==int),"enter the correct type"
        self.name = name
        self.age = age


tst=test( 'aran',12)

# tst=test(12, 'aran')
print(tst.name)
print(tst.age)