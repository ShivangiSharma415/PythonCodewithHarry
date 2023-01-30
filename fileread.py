f = open("shivangi.txt", "rt") #open function returns a file pointer

# data = f.read(3)
# print(data)

# data = f.read(3)
# print(data)

print(f.readlines()) # stores lines in a list

print(f.readline()) # same as below for loop

for line in f:
    print(line, end="")

f.close()