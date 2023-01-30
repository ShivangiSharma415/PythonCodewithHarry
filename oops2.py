class Employee():
    no_of_leaves = 30 #Common to all the objects but if we want to change its value then we can only do using class name

Shivangi = Employee()
Siddhi = Employee()

Shivangi.name = "Sharma"
Shivangi.age = 24

Siddhi.name = "Singh"
Siddhi.age = 23

print(Shivangi.__dict__)
Shivangi.no_of_leaves = 45 #This will not change the value instead it will create a instance variable for shivangi
print(Shivangi.__dict__)
print(Employee.no_of_leaves)