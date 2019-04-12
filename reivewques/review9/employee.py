from band import Band

class Employee(Band):

    employeedict={}
    def __init__(self):
        pass

    def setname(self,name):
        self.name =name

    def setempid(self,empid):
        self.empid = empid

    def createdict(self):
        self.employeedict[self.empid]=[self.name,self.empid,self.band,self.price]

    def getname(self):
        empid=input("enter the Emp id ")
        return self.employeedict[str(empid)][0]

    def getempid(self):
        return self.employeedict[self.empid]

    def getbandvalue(self):
        empid = input("enter the band value: ")
        return self.employeedict[str(empid)][1]

    def getPrice(self):
        empid = input("enter the band value: ")
        return self.employeedict[str(empid)][3]
    
    def updateprice(self):
        empiddetail = input("enter the empid :")
        band=input("enter the band to change :")
        if empiddetail in self.employeedict:
            for i in range(0, len(self.bandlist)):
                if band == self.bandlist[i]:
                    self.employeedict[empiddetail][2] = band
                    self.employeedict[empiddetail][3]= (1200 * i/2)+1200
            else:
                print("enter the correct Band value")
        else:
            print("enter the correct empid value")

employeedetail=Employee()
employeedetail.Assignband(["E01","E02","E03","E04"])
#first Employee
employeedetail.setname("Aravin")
employeedetail.setempid("102")
employeedetail.setPrice("E01")
employeedetail.createdict()
#second Employee
employeedetail.setempid("101")
employeedetail.setname("kevin")
employeedetail.setPrice("E02")
employeedetail.createdict()
#third Employee
employeedetail.setempid("103")
employeedetail.setname("Marn")
employeedetail.setPrice("E02")
employeedetail.createdict()

#Process
print(employeedetail.employeedict)
employeedetail.updateprice()

print(employeedetail.employeedict)

print(employeedetail.getname())