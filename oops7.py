# Inheritance in OOPs
# Single Inheritance

class Employee():
    no_of_leaves = 30
    def __init__(self,aname,aage,asalary):
        self.name = aname
        self.age = aage
        self.salary = asalary


    def printdetails(self): 
        return f"Name is {self.name}. Age is {self.age} and Salary is {self.salary}"


    @classmethod 
    def change_leaves(cls,newleave):
        cls.no_of_leaves=newleave

    @classmethod
    def from_str(cls,string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood():
        print("This is an example of static method")

class Programmer(Employee):
     def printdetailsinheritance(self): 
        return f"Name is {self.name}. Age is {self.age} and Salary is {self.salary}"

Harry = Employee("Harry", 28, 780)
Karan = Employee("Karan", 18, 789)
Shubham = Programmer("Shubham", 43, 900)

print(Shubham.printdetailsinheritance())