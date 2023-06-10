# def function_name_print(a, b, c, d):
#     print(a, b, c, d)

# function_name_print("Shiva", "Shivam", "Shivangi", "Shivi") Ab agar koi or naam bhinadd karna hoga to baar baar argument badhana padega 

# To solve the above problem args parameter ka use krte h or args me chahe list bhejo ya tuple bhejo wo as a tuple hi leta h 

def funargs(*args):
    for item in args:
        print(item)

har = ["Shiva", "Shivam", "Shivangi", "Shivi", "Shivu"]
funargs(*har)

# With this we can pass normal argument also

def funargsnrml(normal, *args):
    for item in args:
        print(item)

har = ["Shiva", "Shivam", "Shivangi", "Shivi", "Shivu"]
normal = "I am a normal argument ans these are my students:"
funargs(normal, *har)

# order of putting argument is normal then args then kwargs
#args and kwargs are optional,apko dena ho to de do ni dena to mat do

def funargs(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)

    print("\nThis is all about kwargs")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")
        # print(type(kwargs))

normal = "I am a normal argument and these are my students:"
har = ["Shiva", "Shivam", "Shivangi", "Shivi", "Shivu"]
kw = {"Shiva":"God", "Shivam":"Pagalu", "Shivangi":"Me"}

funargs( normal,*har,**kw)
