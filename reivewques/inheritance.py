class a:
    def __init__(self,name):
        self.name=name

    def m(self):
        print("A")
class b:
    def m(self):
        print("B")

class c(b,a):
    def m(self):
        print("C")
        super(c,self).m()
        a.m(self)

class d(c,a):

    pass


setattr(d,'name',"saran")

dobj=c
dobj.m()

print(d.name)

'''
class Address:
    def __init__(self, street, city):
        self.street = str(street)
        self.city = str(city)
    def show(self):
        print(self.street)
        print(self.city)

class Person:
    def __init__(self, name, email):
        self.name = str(name)
        self.email= str(email)
    def show(self):
        print(self.name + ' ' + self.email)

class Contact(Person, Address):
    def __init__(self, name, email, street, city):
        Person.__init__(self, name, email)
        Address.__init__(self, street, city)
    def show(self):
        Person.show(self)
        Address.show(self)
        print()

class Notebook:
    people=dict()
    def add(self, name, email, street, city):

        Notebook.people[name] = Contact(name, email, street, city)
        self.nice="0"
        print (id(self.people))
        print (id(Notebook.people))

    def show(self, name):
        if name in self.people:
            self.people[name].show()
        else:
            print('Unknown', name)

notes = Notebook()
notes.add('Alice', '<al@kth.se>', 'Lv 24', 'Sthlm')
notes.add('Bob', '<bb@kth.se>', 'Rtb 35', 'Sthlm')

notes.show('Alice')
notes.show('Carol')
print(notes.people)
print(notes.nice)
'''