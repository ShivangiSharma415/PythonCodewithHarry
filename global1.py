# l = 10 #global variable

# def func1():
#     # l = 5 #local variable
#     m = 9 #local variable
#     #we cannot change the value of global variable , to change it we have to use global keyword
#     global l
#     l = l + 10

#     print(l,m)

# func1()


def harry():
    x = 20
    def rohan():
        global x
        x = 90
    print("Before calling rohan", x)
    rohan()
    print("After calling rohan", x)

harry() # dono function 20 print krenge kyuki global keyword sidhe bahar jata h waha dekhta h
