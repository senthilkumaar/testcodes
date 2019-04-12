from math import pi, e, sin, cos, tan, log, log10, exp, sqrt

class Calculator(object):
    count = 0
    def add(self, num1, num2):
        self.assignvalue = float(num1) + float(num2)
        print("add value:", self.assignvalue)
        sign = input(" ")
        self.count += 1
        return self.calci(sign)

    def sub(self, num1, num2):
        self.assignvalue = num1 - num2
        print("sub value:", self.assignvalue)
        sign = input(" ")
        self.count += 1
        return self.calci(sign)

    def mul(self, num1, num2):
        self.assignvalue = num1 * num2
        print("mul value:", self.assignvalue)
        sign = input(" ")
        self.count += 1
        return self.calci(sign)

    def div(self, num1, num2):
        self.assignvalue = float(num1 / num2)
        print("div value:", self.assignvalue)
        sign = input(" ")
        self.count += 1
        return self.calci(sign)

    def sin(self,num):
        self.assignvalue = sin(float(num))
        sign = input(" ")
        self.count += 1
        return self.calci(sign)

    def cos(self,num):
        self.assignvalue = cos(num)
        sign = input(" ")
        self.count += 1
        return self.calci(sign)

    def tan(self,num):
        self.assignvalue = tan(num)
        sign = input(" ")
        self.count += 1
        return self.calci(sign)

    def cot(self,num):
        self.assignvalue = 1/tan(num)
        sign = input(" ")
        self.count += 1
        return self.calci(sign)

    def cosec(self,num):
        self.assignvalue = 1/sin(num)
        sign = input(" ")
        self.count += 1
        return self.calci(sign)

    def sec(self,num):
        self.assignvalue = 1/cos(num)
        sign = input(" ")
        self.count += 1
        return self.calci(sign)

    def printvalue(self):
        print(self.assignvalue)



