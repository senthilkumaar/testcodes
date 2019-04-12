class books:
    weight=0
    no_of_books=0
    def __init__(self,name,price,weight):
        self.name=name
        self.price=price
        self.weight=weight
        # books.weight+=weight
        # books.no_of_books+=1

    def display_Price(self):
        return self.price

    @classmethod
    def no_of_copies(cls,name,price,quantity,weight,type):
        cls.type=type
        return cls(name,price*quantity,weight)

    @staticmethod
    def book_Weight(weight):
        return weight

    def __del__(self):
        books.no_of_books-=1
        print("books shredded")
        return "success"

class Enggbook(books):
    def __init__(self,name,price,subject,weight):
        books.__init__(self,name,price,weight)
        print(self.name)
        print(price)
        self.subject=subject


    # def display_Price(self,n):
    #     return 2*selfprice*n

    # def display_Price(self,n):
    #     return self.price*n

    def display_Price(self,n):
        return self.price*n

class Medical(books):
    def __init__(self,name,subject,price,weight):
        books.__init__(self,price,name,weight)
        self.subject=subject

    def display_Price(self):
        return self.price*4


engg = Enggbook("ADC",210,"computer",120)
med = Medical("psyiology",310,"anotomy",250)
print("Engg book details")
print("name:",engg.name)
print("weight:",engg.book_Weight())
print("cost:",engg.display_Price(5))

print("med book details")
print("name:",med.subject)
print("weight:",med.weight)
print("cost:",med.display_Price())

print("class and Staic keyword usauge")
cost_of_quotes=books.no_of_copies("harry potter",650,10,160,"magic")
print(cost_of_quotes.price)
print(cost_of_quotes.weight)
print(cost_of_quotes.type)
# print(med.cost_of_quotes.price)                      ##########unable to call this ciz Medical' object has no attribute 'cost_of_quotes'
print(books.book_Weight())
print(books.no_of_books)

del cost_of_quotes
