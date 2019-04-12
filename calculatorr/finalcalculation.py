from calculatorr.calculator import Calculator

class Finalcalculation(Calculator):

    def __init__(self):
        functions = ['sin', 'cos', 'tan']
        self.num1 = input(' ')
        self.sign = input(' ')
        if self.num1 in functions:
            self.calci(self.num1)
        else:
            self.num2 = input(' ')
            self.calci(self.sign)


    def calci(self,sign):

        if self.count < 1:
            if sign == "+":
                self.add(self.num1,self.num2)

            elif sign == "-":
                self.sub(self.num1, self.num2)

            elif sign == "*":
                self.mul(self.num1, self.num2)

            elif sign == "/":
                self.div(self.num1, self.num2)

            elif sign == "sin":
                self.sin(int(self.sign))

            elif sign == "=" or self.num2 == "=":
                self.printvalue()

        elif self.count > 0:
            if sign == "+":
                num2 = int(input(" "))
                self.add(self.assignvalue, num2)

            elif sign == "-":
                num2 = int(input(" "))
                self.sub(self.assignvalue, num2)

            elif sign == "*":
                num2 = int(input(" "))
                self.mul(self.assignvalue, num2)

            elif sign == "/":
                num2 = int(input(" "))
                self.div(self.assignvalue, num2)

            elif sign == "sin":
                self.sin(int(self.sign))

            elif sign == "=":
                self.printvalue()

calc=Finalcalculation()