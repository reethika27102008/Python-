# name="Python Programming"
# # print(len(name))
# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name.casefold())
# print(name.center(25))
# print(name.index("g"))
# print(name[0:10])
# print(name[5:])
# print(name[:10])

# Task1 write a program to count the vowel letter from the given string 
# n=(input("Enter a name:"))
# count=0
# for i in (n):
#  if i in "aeiou":
#   count+=1
# print(count)

# Task2 write a program to rev the given string
# n=input("Enter a word:")
# rev=""
# for i in (n):
#     rev=i+rev
# print(rev)   

# Task3 write a program ton find the palindrome
# n=input("Enter a word:").upper()
# rev=""
# for i in (n):
#     rev=i+rev
# if n==rev:
#         print("It is a palindrome")
# else:
#         print("It is not a palindrome")

# Task4 write a program to count a upper and lower case in the given string

# n = input("Enter a word: ")
# count1 = 0
# count2 = 0
# for i in n:
#     if i.isupper():
#         count1+= 1
#     elif i.islower():
#         count2 += 1
# print("Uppercase count:", count1)
# print("Lowercase count:", count2)

# Task5 write a program to ignore space

# n=input("Enter your word:")
# rev="" 
# for i in n:
#     if i!= " ":
#         rev+=i
# print(rev)

# Task6 write a program to check the frequency of the string

# n = input("Enter a string: ").upper()
# count = ""
# for i in n:
#     if i not in count:
#         print(i, ":", n.count(i))
#         count += i

# # Task7 write a to count the digit
# n=(input("Enter your number:"))
# count=0
# for i in (n):
#     if i.isnumeric():
#      count+=1      
# print("Number of digits",count)
    
# Task8 8. Write a program to check if a string contains only alphabetic characters.
# n=input("Enter your word:")
# for i in (n):
#     if ('a' <=i <= 'z') or ('A' <= i <= 'Z'):
#      print(i,"It is a alphabet")
    
#Task 9  Write a program to convert all lowercase letters in a string
#  to uppercase manually using ASCII values.

# n=input("Enter your value:")
# result=""
# for i in n:
#     if ('a' <= i <= 'z'):
#        result+=chr((ord(i)-32))
# print(result)

# Task10
# n=input("Enter a word:")
# for i in range(0,len(n),2):
#     print(n[i])

# Task11 Write a program to count the number of words in a string without using split().

# n=input("Enter your sentence:")
# count=1
# for i in n:
#     if i==" ":
#         count+=1
# print("Number of words are",count)

# Task12 write a program to replace vowel with *

# n = input("Enter your value: ")
# for i in "aeiou":
#     n = n.replace(i, "*")
# print(n)

# Task13 Write a program to find the longest word in a sentence
# s = input("Enter a sentence: ")
# count = ""
# for w in s.split():
#     if len(w) > len(count):
#         count = w
# print("Longest word is:",count)    

# Task14 
# n1 = input("Enter first word: ")
# n2 = input("Enter second word: ")
# count = 0
# for i in n1:
#     if i in n2:
#         count += 1
# if count == len(n1):
#     print("It is an anagram")
# else:
#     print("It is not an anagram")


# Task15
# n = input("Enter your sentence: ")
# count = 0
# for i in n:
#     if not i.isalnum() and i!=" ":
#         count += 1
# print(count, "special characters in your sentence")

# Task16
# n=input("Enter your word:")
# n1=int(input("Enter the required times:"))
# for i in n:
#     print(i*n1,end="")

# task17
# n= input("Enter a string: ")
# result = ""
# for i in n:
#     if i not in result:
#         result+=i
# print("After removing duplicates:", result)

# Task18
# n=input("Enter youe sentence:")
# result=0
# for i in n:
#      if i not in "aeiou":
#           result+=1
# print(result,"number of consonants ")
          
# # Task19
# n=input("Enter your sentence:")
# print(n[0].upper()+ n[1:])


# Task20
n=input("Enter your value")
count=0
for i in n:
    if i in "aeiou":
        count+=1
print(count,"vowels are there")