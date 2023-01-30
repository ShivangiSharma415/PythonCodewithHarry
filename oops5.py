class Employee():
    no_of_leaves = 30
    def __init__(self,aname,aage,asalary):
        self.name = aname
        self.age = aage
        self.salary = asalary


    def printdetails(self): #self matlab wo object jispe ye function lagega
        return f"Name is {self.name}. Age is {self.age} and Salary is {self.salary}"


    @classmethod #srf class k instance variable ko use kar sakta h
    def change_leaves(cls,newleave):
        cls.no_of_leaves=newleave

    @classmethod
    def from_str(cls,string):
        # params = string.split("-")
        # return cls(params[0], params[1], params[2])
        #Alternative to above 2 lines is written below
        return cls(*string.split("-"))




Shivangi = Employee("Shivangi",23,500) #Employee ko arguments dene k tarike ko constructor kahte h,uske liye init method banana hoga
Siddhi = Employee("Siddhi", 22,500)
karan = Employee.from_str("Karan-29-870") #Using alternative constructor

print(karan.salary)

# Employee.change_leaves(45)

# print(Shivangi.no_of_leaves)