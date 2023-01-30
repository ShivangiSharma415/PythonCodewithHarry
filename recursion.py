# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n* factorial(n-1)

# num = int(input())
# print(factorial(num))

# # iterative approach
# def fact_iter(n):
#     fact = 1
#     for i in range(n):
#         fact = fact * (i+1)
#     return fact

# num1= int(input())
# print(fact_iter(num1))

#fibonacci series
def fibbo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibbo(n-1) + fibbo(n-2)

num = int(input())
print(fibbo(num))