# #Built in functions.
# a = 8
# b = 8
# c = sum((a,b)) #argument must be either list,tuple  etc i.e. it must be iterable
# print(c)

# #User Defined Function

# def func1(a,b):
#     print("Sum is:", a+b)

# func1(5,8)

def func2(a,b):
    #Function k andar jo pahli line of string likhi hui hoti hai use kahte hai docstring
    """This is a doctstring"""
    avg=(a+b)/2
    return avg

ans = func2(8,7)
print(ans)
print(func2.__doc__)

#Argument and return type is optional
#If the function doesnot return anything then it is considered to be returning None