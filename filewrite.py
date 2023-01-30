# f = open("shivangi1.txt", "w")
# len = f.write("\nShivangi Sharma Information Technology\n")
# print(len)

# f = open("shivangi2.txt", "a")
# len = f.write("\nShivangi Sharma Information Technology\n")
# print(len)

# f.close()

# Handle read and write both

f = open("shivangi1.txt", "r+")

print(f.read())

f.write("Batch 2022")