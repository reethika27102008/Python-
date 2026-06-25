#  task1  Write a Python program to print all elements of a list using a loop.

# list=[12,13,14,15,16,17]
# def displayfun(num):
#     for i in num:
#         print(i)
# displayfun(list)

# Task2  Write a Python program to print only the even numbers from a list.
# list=[12,13,14,15,16,17]
# def displayfunc(num):
#     for i in list:
#         if i%2==0:
#             print(i)
# displayfunc(list)

#  Task3  Write a Python program to print only the even numbers from a list.
# list=[12,13,14,15,16,17]
# def displayfunc(num):
#     for i in list:
#         if i%2!=0:
#             print(i)
# displayfunc(list)


# Task4 write a program to print number from 1 to 10
# def displaynum(num):
#     for n in range(1,11):
#         print(n)
# displaynum(range)

# task5 writa a program to print numbers all even numbers from 1 to 20 
# def displaynum(num):
#     for n1 in range(21):
#         if n1%2==0:
#             print(n1)
# displaynum(range)

# task6 writa a program to print numbers all odd numbers from 1 to 20 
# def displaynum(num):
#     for n1 in range(21):
#         if n1%2!=0:
#             print(n1)
# displaynum(range)

# Task7 Write a program to print number from 10 to 1
# def displaynum(num):
#     for n3 in range(10,0,-1):
#       print(n3)
# displaynum(range)

# Task8 Writa a program to print 7 table
# def displaytab(table):
#    for n9 in range(1,11):
#     print("7 x",n9 ,"=" ,n9*7)
# displaytab(range)


# Task 9 Write a program to find odd,even and zero

# n4=int(input("Enter your number:"))
# def display(num):
#    if  num==0:
#     print("It is Zero")
#    elif  num%2 == 0:
#     print("It is a Even number")
#    else:
#     print("It is a odd number")
# display(n4)

# Task 10 Write a progarm to find negative, positive and zero

# x=int(input("Enter your number:"))
# def display(num):
#    if num>0:
#     print("It is a postive number")
#    elif num<0:
#     print("It is a negative number")
#    else:
#     print("It is Zero")
# display(x)





a=10
def myfunction():
    global a
    a=5
    print(a)
myfunction()
print(a)
