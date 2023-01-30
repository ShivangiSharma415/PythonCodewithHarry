# class Employee():
#     no_of_leaves = 30

#     def printdetails(self): #self matlab wo object jispe ye function lagega
#         return f"Name is {self.name}. Age is {self.age} and Salary is {self.salary}"



# Shivangi = Employee()
# Siddhi = Employee()

# Shivangi.name = "Sharma"
# Shivangi.age = 24
# Shivangi.salary = 500

# Siddhi.name = "Singh"
# Siddhi.age = 23
# Siddhi.salary = 500

# print(Shivangi.printdetails()) 

#Constructor
class Employee():
    no_of_leaves = 30
    def __init__(self,aname,aage,asalary):
        self.name = aname
        self.age = aage
        self.salary = asalary


    def printdetails(self): #self matlab wo object jispe ye function lagega
        return f"Name is {self.name}. Age is {self.age} and Salary is {self.salary}"



Shivangi = Employee("Shivangi",23,500) #Employee ko arguments dene k tarike ko constructor kahte h,uske liye init method banana hoga
# Siddhi = Employee()

print(Shivangi.salary)