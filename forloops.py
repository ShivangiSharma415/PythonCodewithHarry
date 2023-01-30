# list1 = ["Shiv", "Shiva", "Shivam", "Shivangi"]
# # list and tuple both can be iterated in the same way

# for item in list1:
#     print(item)

# list2 = [["Shiv", 1], ["Shiva", 2], ["Shivam", 3], ["Shivangi", 4]] #list of list

# # for item in list2:
# #     print(item)

# # for item, lollipop in list2:
# #     print(item,lollipop)

# dict1 = dict(list2)
# # print(dict1)

# #to get only key
# for key in dict1:
#     print(key)

# for item, toffee in dict1.items():
#     print(item,toffee)


l1 = [ 1 ,8 ,6, 89, 90 ,98, 78, 65,45,]
for i in l1:
    if str(i).isnumeric() and i>7:
        print(i)
