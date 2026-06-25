# Task 1. Create a tuple that contains an integer, a string, and a float.

# myTuple=(12.214,"reethika",3456,True)

# Task2. Access the second element of the tuple (5, 10, 15, 20).
# myTuple=(12.214,"reethika",3456,True)
# print(myTuple[1])

# TASk3. Slice the tuple (1, 2, 3, 4, 5) to get the last two elements.
# mytuple = (100, 34, 67, 12, 58, 90)
# print(mytuple[-2:])

# Task4. Concatenate the tuples (1, 2) and (3, 4).
# tuple1=(1,2)
# tuple2=(3,4)
# result= tuple1+tuple2
# print(result)

# Task5. Repeat the tuple (7, 8) three times.
# tuple=(7,8)
# result= tuple*3
# print(result)

# Task6. Check if 15 is present in the tuple (10, 20, 15, 25).
# tuple = (10, 20, 15, 25)
# if 15 in tuple:
#         print("15 is present in this tuple")
# else:
#         print("15 is not present in this tuple")


# Task 7. Find the length of the tuple (3, 6, 9, 12).
# tuple =(3, 6, 9, 12)
# print(len(tuple))


# Task8. Find the maximum and minimum values in the tuple (4, 1, 8, 3).

# tuple = (4, 1, 8, 3)

# print("Maximum value:", max(tuple))
# print("Minimum value:", min(tuple))

# Task9. Convert the list [1, 2, 3, 4] into a tuple.
# list =[1, 2, 3, 4]
# typecasting=tuple(list)
# print(typecasting)

# Task10. Convert the tuple (10, 20, 30) into a list.
# tuple =(10, 20, 30)
# typecasting=list(tuple)
# print(typecasting)

# Task11. Find the index of the element 30 in the tuple (10, 20, 30, 40).
# tuple =(10, 20, 30, 40)
# print(tuple.index(30))

# Task12. Count how many times 2 appears in the tuple (2, 3, 2, 4, 2).
# tuple =(2, 3, 2, 4, 2)
# count=0
# for i in tuple:
#     if i==2:
#         count+=1
# print("There are ", count , "in this tuple")

# Task13. Unpack the tuple (100, 200, 300) into three separate variables.
# tuple= (100, 200, 300)
# a,b,c=tuple
# print(a)
# print(b)
# print(c)

# Task14. Swap the values of two tuples (1, 2) and (3, 4).
# tuple1= (1, 2) 
# tuple2=(3,4)
# tuple1,tuple2=tuple2,tuple1
# print("tuple1=", tuple1)
# print("tuple2=",tuple2)

# TASk15. Create a tuple that contains two other tuples (1, 2) and (3, 4).
# tuple = ((1,2),(3,4))
# print(tuple)

# TASk16. Access the number 4 from the nested tuple ((1, 2), (3, 4)).
# tuple= ((1, 2), (3, 4))
# print(tuple[1][1])

# TAsk17. Find the sum of all numbers in the tuple (5, 10, 15).
# tuple= (5, 10, 15)
# sum=0
# for i in tuple:
#     sum+=i
# print("The sum of the tuple",sum)

# TAsk 18. Sort the elements of the tuple (40, 10, 30, 20) in ascending order.
# tuple= (40, 10, 30, 20)
# type=list(tuple)
# type.sort()
# print(type)


# Task19) Reverse the elements of the tuple (1, 2, 3, 4, 5).
# tuple =(1, 2, 3, 4, 5)
# type=list(tuple)
# type.reverse()
# print(type)


# TASk 20) Check if all elements in the tuple (5, 5, 5, 5) are identical.
t = (5, 5, 5, 5)
for i in t:
    if i != t[0]:
        print("the elements are not identical")
        break
else:
    print("the elements are identical")    
    
    