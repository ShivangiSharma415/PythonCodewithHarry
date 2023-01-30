# Classes - Template
# Object - Instance of the class

# DRY - Do Not Repeat Yourself

class student(): #class
    pass

harry = student()
larry = student() # created two objects of the class

# we can create instance variable of the objects
harry.name = "Harry"
harry.age = 17
larry.std = 9
larry.subjects = ["physics","maths"]
print(harry.name, harry.age)
print(larry.std, larry.subjects)

