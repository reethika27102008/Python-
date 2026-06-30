# Task 1
x=int(input("Enter your number:"))
if x>0:
    print("It is a postive number")
elif x<0:
    print("It is a negative number")
else:
    print("It is Zero")
#  Task 2
n1= int(input("Enter value 1:"))
n2= int(input("Enter value 2:"))
n3= int(input("Enter value 3:"))
if n1>=n2 and n1>=n3:
    print("The greatest number is:", n1)
elif n2>=n1 and n2>=n3:
    print("The greatest number is: ", n2)
else:
    print("The greatest number is:", n3)
# Task 3
y=int(input("Enter your marks:"))
if y>=0 and y<=70:
    print("You scored c Grade")
elif y>=71 and y<=80:
    print("0 You scored B Grade")
else:
    print(" You scored A grade")
# Task 4
n4=int(input("Enter your number:"))
if  n4==0:
    print("It is Zero")
elif  n4%2 == 0:
    print("It is a Even number")
else:
    print("It is a odd number")
# Task5
L1=int(input("Enter your first length :"))
L2=int(input("Enter your second length: "))
L3=int(input("Enter your third length: "))
if L1==L2==L3:
    print("Equilateral Triangle")
elif L1 == L2 or L1 == L3 or L2==L3:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
# Task6
val1=int(input("Enter first value:"))
val2=int(input("Enter second value:"))
oper=input("Enter the required opeartor:")
if oper=="+":
    print("The sum of two digit is ",val1+val2)
elif oper=="-":
    print("The subtraction of two digit is",val1-val2)
elif oper=="*":
    print("The multiplication of two digit is",val1*val2)
elif oper=="/":
     print("The division of two digit is",val1/val2)
elif oper=="//": 
     print("The answer is",val1//val2)  
elif oper=="%": 
    print("The modulus of two digit is",val1%val2)
else:
    print("ERROR!! PLEASE CHECK YOUR NUMBER")                      
          
          
          
          
          
          
          
          
          
          
          
          
          