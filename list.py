# task1  Write a Python program to print all elements of a list using a loop.

# list=[12,13,14,15,16,17]
# for i in list:
#     print(i)

# Task2  Write a Python program to print only the even numbers from a list.
# list=[12,13,14,15,16,17]
# for i in list:
#     if i%2==0:
#         print(i)


# Task3 Write a Python program to print only the odd numbers from a list.

# list=[12,13,14,15,16,17]
# for i in list:
#     if i%2!=0:
#         print(i)

# task4 Write a Python program to find the sum of all numbers in a list.


# list=[23,12,35,67,765,54,43,1]
# sum=0
# for i in list:
#     sum+=i
# print(sum)

# Task5 Write a Python program to find the largest number in a list using a loop# 
# list=[23,12,35,67,765,54,43,1]
# largest=list[0]
# for i in list:
#     if i>largest:
#         largest=i
# print(largest)

# Task6
# list=[23,12,35,67,765,54,43,1]
# smallest=list[0]
# for i in list:
#     if i<smallest:
#         smallest=i
# print(smallest)


# # Task7 Write a Python program to count how many positive numbers are in a 
# list=[23,-12,35,-67,-765,-54,43,1]
# count=0
# for i in list:
#     if i>=0:
#         count+=1
# print("The number of positive numbers:",count)


# Task8 Write a Python program to count how many negative numbers are in a list.

# list=[23,-12,35,-67,-765,-54,43,1,234]
# count=0
# for i in list:
#     if i<0:
#         count+=1
# print("The number of negative numbers:",count)

# task9 Write a Python program to reverse a list without using the .reverse() method.

# list=[23,-12,35,-67,-765,-54,43,1,234]
# reserved=list[::-1]
# print(reserved)

# Task10 Write a Python program to count how many even and odd numbers are present in a list.

# count1=0
# count2=0
# list=[23,-12,35,-67,-765,-54,43,1,234]
# for i in list:
#     if i%2==0:
#         count1+=1
#     elif i%2!=0:
#         count2+=1
# print("The number of even numbers is ",count1)
# print("The number of odd numbers is",count2)


# Task11 Write a Python program to find and print the index of a specific value in a list.

# list = [23, -12, 35, -67, -765, -54, 43, 1, 234]
# n = int(input("Enter your value: "))
# if n in list:
#     x = list.index(n)
#     print("The index of", n, "is", x)
# else:
#     print("Value not found in the list")

# task 12 Write a Python program to replace all negative numbers in a list with 0.

# mylist=[23,-12,35,-67,-765,-54,43,1,234]
# for i in range(len(mylist)):
#     if  mylist[i]<0:
#         mylist[i]=0
# print(mylist)


# Task13 
# mylist=[23,-12,35,-67,-765,-54,51,55,43,1,234]
# for i in range(len(mylist)):
#     if mylist[i]>50:
#         print(mylist[i])

# Task14

# mylist=[10,1,2,4,5,67,25,6,5]
# square=[]
# for i in mylist:
#     square.append(i**2)
# print(square)


# Task15. Write a Python program to print all duplicate values in a list.
# mylist = [1, 2, 3, 2, 4, 5, 1, 6]
# newlist=[]
# for x in mylist:
#     if mylist.count(x) > 1:
#         if x not in newlist:
#          newlist.append(x)
# print(newlist)
    
# Task16 Write a Python program to print list elements until the number 50 appears (stop when found).
# mylist = [1, 2, 3, 2,4, 5,50, 1, 6]
# for i in mylist:
#     if i>=50:
#         break
#     print(i)

# Task17 Write a Python program to count how many numbers in a list are divisible by 5.
# mylist = [1, 2, 30, 24,4, 5,50, 45, 65]
# count=0
# for i in mylist:
#     if i%5==0:
#         count+=1
# print("There are",count, "numbers divisible by 5")

# Task18. Write a Python program to find the second largest number in a list using loops
#  mylist=[1,2,12,24.4, 5, 50, 45, 65]
# for i in range(2):
#     largest = mylist[0]
#     for i in mylist:
#         if i > largest:
#             largest = i
#     mylist.remove(largest)
# print(largest)

# Task19. Write a Python program to check whether a list is sorted in ascending order.
# mylist = [12, 22, 345, 56, 13, 134, 124, 634]
# for i in range(len(mylist) - 1):
#     if mylist[i] > mylist[i + 1]:
#         print("The list is not sorted")
#         break
# else:
#     print("The list is sorted")

# Task20. Write a Python program to find the sum of only the even numbers in a list.

mylist = [18, 42, 7, 91, 35, 12, 68, 24]
sum=0
for i in mylist:
    if i%2==0:
        sum+=i
print("the sum of even number is",sum)