# me = "Shivangi"
# # a = "This is %s"%me
# a1 = 5
# a = "This is {} {}"
# b = a.format(me,a1)
# print(b)
#This formatting concept is not readable therefore we use the concept of Fstrings
import math

me = "Shivam"
a1 = 8
a = f"This is {me} {a1} {2*8}"
b = f"This is {me} {a1} {math.factorial(8)}"
print(a)
print(b)
