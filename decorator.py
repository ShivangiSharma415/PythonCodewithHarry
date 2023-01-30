# def func1():
#     print("Hello,This is Shivangi")

# func2 = func1
# #Now even if we delete func1 and then call func2 ,then also it will print Hello.......
# del func1
# func2()


#We can also return a function through a function
# def funcreturn(num):
#     if num==1:
#         return print
#     if num==2:
#         return sum

# a = funcreturn(2)
# print(a)


def dec1(func1):
    def execute():
        print("Before Hello")
        func1()
        print("After Hello")
    return execute

@dec1
def try_this():
    print("Shivangi Sharma")

# try_this = dec1(try_this) # Instead of this line we can write @dec1 before try_this function
try_this()