# task1 Write a Python program to print numbers from 1 to 20 and 
# stop when the number reaches 10 using break.

# for i in range (1,20):
#     print(i)
#     if i==10:
#         break

# Task2  Write a Python program to print numbers from 1 to 15 except 8 using continue.

# for i in range(1,16):
#     if i==8:
#         continue
#     print(i)

# task3 3) Write a Python program to print numbers from 1 to 50 and 
# stop when the first multiple of 7 greater than 20 is found.

# for i in range(1,51):   
#     print(i)
#     if i%7==0 and i>20:
#         break
    

# Task4 Write a Python program to print all odd numbers from 1 to 30 by skipping even numbers.
# for i in range(1,31):
#     if i%2==0:
#         continue
#     print(i)


# Task5 5)Write a Python program to keep adding natural numbers starting from
#  1 and stop when the sum exceeds 100.
# sum=0
# for i in range(1,100):
#     sum+=i
#     print(sum)
#     if sum>=100:
#         break


# Task6 Write a Python program to print numbers from 1 to 25 except the multiples of 3.

# for i in range(1,25):
#     if i%3==0:
#         continue
#     print(i)


# Task7 Write a Python program to print the multiplication table of 5 and stop after 5 × 7.

# num=0
# for i in range(1,10):
#     num+=1
#     print("5 x",num,"=",5*num)
#     if num==7:
#         break


# Task8  Write a Python program to print numbers from 1 to 100 and 
# stop when the first number divisible by 11 is found.


# for i in range(1,100):
#     print(i)
#     if i%11==0:
#         break


# Task9 Write a Python program to print numbers from 1 to 20 while skipping all even numbers.

# for i in range(1,20):
#     if i%2==0:
#         continue
#     print(i)

# Task10 Write a Python program to print numbers from 1 to 50 and 
# skip all numbers ending with the digit 5.


# for i in range(1,50):
#     if i%10==5:
#         continue
#     print(i)


# Task11 Write a Python program to find the first prime number greater than 50 and stop after finding it.
# for i in range(51, 55):
#     prime = True
#     for k in range(2, i):
#         if i % k == 0:
#             prime = False
#             break
#     if prime:
#         print(i)
#         break

    
# TAsk12  Write a Python program to print numbers from 1 to 30 
# except those divisible by 2 or 3.

# for i in range(1,31):
#     if i%2==0 or i%3==0:
#         continue
#     print(i)


# Task13 13) Write a Python program to print the characters of a string and
# #  stop when the character 'x' is encountered.
# n=input("Enter your word:")
# for i in n:
#     if i=="x":
#         break
#     print(i,end="")


# Task14 Write a Python program to print all characters of a string except vowels.

# n=input("Enter youre sentences:")
# for i in n:
#     if i in "aeiouAEIOU":
#         continue
#     print(i,end="")

# Task15 Write a Python program to print all characters of a sentence except spaces.


# n=input("Enter youre sentences:")
# for i in n:
#     if i in " ":
#         continue
#     print(i,end="")

# Task 16 Write a Python program to count vowels in a string and 
# stop counting when a space is encountered.

# n=input("Enter youre sentences:")
# count=0
# for i in n:
#     if i in "aeiouAEIOU":
#         count+=1
#     elif i in " ":
#         break
# print("The number of vowel",count)


# Task17  Write a Python program to print only uppercase letters from a given string.

# n = input("Enter a string: ")
# for i in n:
#     if i.isupper():
#         print(i)
    

# Task 18 Write a Python program to print only lowercase letters 
# from a given string by skipping uppercase letters.


# n = input("Enter a string: ")
# for i in n:
#     if i.isupper():
#         continue
#     print(i,end="")
  

# Task19 Write a Python program to read numbers from the user continuously and
#  stop when 0 is entered.


# for i in range(100): 
#     n = int(input("Enter a number: "))
#     if n == 0:
#         break
#     print("You entered:", n)
# print("Program stopped.")


# Task20  Write a Python program to allow only three password attempts and
#  stop when the correct password is entered.

# password = "reethika"
# for i in range(3):
#     n = input("Enter your password: ")
#     if n == password:
#         print("Correct password")
#         break
# else:
#     print("Incorrect password")


# Task21 Write a Python program to continuously accept 
# user input and terminate when the user enters "exit".

# for i in range(100):  
#     text = input("Enter your sentence: ")
#     if text == "exit":
#         break
#     print("You entered:", text)
# print("Thank you for using python.")



# Task22 Write a Python program to print numbers from 1 to 100 and 
# stop when the square of a number exceeds 500.

# for i in range(1,100):
#     result=i*i
#     if result>=500:
#         break
#     print("The square of ",i,"is ",result)


# Task23  Write a Python program to print numbers from 1 to 40, skipping multiples of 4.

# for i in range(1,40):
#     if i%4==0:
#         continue
#     print(i)

# Task24 Write a Python program to print odd numbers from 1 to 50 and
#  stop when the number exceeds 35.

# for i in range(0,50,2):
#     if i>35:
#         break
#     print(i)


# task25  Write a Python program to display the multiplication table of 8 
# while skipping the multiples corresponding to multipliers 3 and 6.

# for i in range(1,11):
#     if i==3 or i==6:
#         continue
#     print("8x",i,"=",8*i)

# Task26 Write a Python program to print numbers from 1 to 30 
# skipping numbers divisible by 5, and stop when the number reaches 25.



# for i in range(1,30):
#     if i==25:
#         break
#     elif i%5==0:
#         continue
#     print(i)


# Task27 Write a Python program to print characters of a string and 
# stop when the first digit is encountered.

n=int(input("Enter your sentences:"))
for i in n:
    if i.isdigit():
        break
    print(i,end="")