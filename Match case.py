# task 1
# Value=int(input("Enter your number:"))
# match Value%2==0:
#     case True: 
#         print("It is a Even number")
#     case False:
#         print("It is a odd number")
# Task2
# value2=int(input("Enter your value:"))
# match value2:
#     case _ if value2 > 0:
#         print("It is a positive number")
#     case _ if value2 < 0:
#         print("It is a negative number")
#     case _:
#         print("Zero")
# Task3
# value3=int(input("Enter first value:"))
# value4=int(input("Enter second value:"))
# operator=(input("Enter any operator:"))
# match operator:
#     case _ if operator=="+":
#         print("The answer is",value3+value4)
#     case _ if operator=="-" :
#         print("The answer is",value3-value4)
#     case _ if operator=="*":
#         print("The answer is",value3*value4)
#     case _ if operator=="/":
#         print("The answer is",value3/value4)
#     case _ if operator=="%":
#         print("The answer is",value3%value4)
#     case _  : 
#         print("The answer is",value3//value4)
# Task4
# days=input("Enter a day:")
# match days:
#     case  "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday" :
#         print("It is a weekday")
#     case "Saturday" | "Sunday":
#         print("It is a weekend")
# Task5
# n1=int(input("Enter your marks:"))
# match n1:
#     case _ if n1>=90:
#         print("You scored A grade")
#     case _ if n1>=70:
#         print("You scored B grade")
#     case _ if n1>=60:
#         print("You scored C grade")
#     case _ if n1>35:
#         print("You scored D grade")
#     case _:
#         print("You failed")
# Task6
#  month=int(input("Enter your month number"))
# match month:
#     case 1:
#         print("January")
#     case 2:
#         print("February")
#     case 3:
#         print("March")
#     case 4:
#         print("April")
#     case 5:
#         print("May")
#     case 6:
#         print("June")
#     case 7:
#         print("July")
#     case 8:
    #     print("August")
    # case 9:
    #     print("September")
    # case 10:
    #     print("October")
    # case 11:
    #     print("November")
    # case 12:
    #     print("December")
    # case _:
    #     print("Invaild number")
# task7
# alpha=input("Enter your alphabet:")
# match alpha:
#     case "a"|"e"|"i"|"o"|"u":
#         print("It is a vowel letter")
#     case _:
#         print("It is a consonant")
# task8
# signal=input("Enter the signal colour:")
# match signal:
#     case "Red":
#         print("Stop")
#     case "Yellow":
#         print("Wait")
#     case "Green":
#         print("Go")
#     case _:
#         print("Invalid colour")
# Task9
# leap=int(input("Enter your year:"))
# match leap % 4:
#     case 0:
#         print("It is a leap year")
#     case _ :
#         print("Not a leap year")
# task10
# age=int(input("Enter your age:"))
# match age:
#     case _ if age<=10:
#         print("You are an child" )
#     case _ if age<=18:
#         print("You are an teenager")
#     case _ if age<=50:
#         print("Adult")
#     case _ :
#         print("Senior")
# Task11
# num=int(input("Enter number between 1 to 10:"))
# match num:
#     case 1:
#         print("You enter the number 1")
#     case 2:
#         print("You enter the number 2")
#     case 3:
#         print("You enter the number 3")
#     case 4:
#         print("You enter the number")
#     case 5:
#         print("You enter the number 5")
#     case 6:
#         print("You enter the number 6")
#     case 7:
#         print("You enter the number 7")
#     case 8:
#         print("You enter the number 8")
#     case 9:
#         print("You enter the number 9")
#     case 10:
#         print("You enter the number 10")
#     case _:
#         print("Invalid number")
# task 12
# db_email="reethika2008@gmail.com"
# db_password="reethi@2008"
# email=input("Enter your email:")
# password=input("Enter your password:")
# match email,password:
#     case _ if "reethika2008@gmail.com" and "reethi@2008":
#         print("login successful")
#     case _ if "reethika2008@gmail.com"|"":
#         print("Password incorrect")
#     case _ if ""|"reethi@2008":
#         print("email incorrect")
#     case _:
#          print("login unsuccessful")
# task13
# side=int(input("Enter the number of side:"))
# match side:
#     case 3:
#         print("Triangle")
#     case 4:
#         print("Quadrilateral")
#     case 5:
#         print("Pentagon")
#     case 6:
#         print("Hexagon")
#     case 7:
#         print("Heptagon")
#     case 8:
#         print("Octagon")
#     case 9:
#         print("Nonagon")
#     case 10:
#         print("Decagon")
#     case 11:
#         print("Hendecagon")
#     case 12:
#         print("Dodecagon")
#     case _:
#         print("Shape not available")
# Task14
# number=int(input("Enter a number:"))
# match number:
#     case _ if number%3==0 and number%5==0:
#         print("The given number is divisible by both 3 and 5")
#     case _:
#         print("The given number is  not divisible by both 3 and 5")
# Task 15
num2=int(input("Enter the number:" ))
match num2:
    case 0:
        print("The given number is 0")
    case _ if num2>0 and num2%2==0:
        print("The given number is a Positive even")
    case _ if num2<0 and num2%2==0:
        print("The given number is a negative even")
    case _:
        print("Invaild number")