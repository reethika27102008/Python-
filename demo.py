from functools import reduce
# read a file
file = open("demo.txt", "r")
# data = file.read()
# data = file.readline()
data = file.readlines()
print(data)


# # Write a existing file
# file=open("demo.txt","w")
# content="File handling"
# file.write(content)
# print("sucessful")

# # Write a new file
# file=open("newfile.txt","w")
# content="Hello world"
# file.write(content)

# file=open("dem.txt","x")
# content="file handling is easy"
# file.write(content)


# file=open("demo.txt","a")
# content="File handling is not easy"
# file.write(content)

# import os
# os.rename("dem.txt","test.txt")
# os.mkdir("Filehandling")
# os.remove("newfile.txt")

num=[4, 10, 7, 25, 3]
maximum = reduce(lambda x,y: max(x,y), num)
print(maximum)
