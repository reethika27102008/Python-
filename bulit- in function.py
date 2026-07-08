from functools import reduce
# # map,filter,reduce

# # mapping function

# # Task.Use map() to double each number in the list [1, 2, 3, 4, 5].
# # numbers = [1, 2, 3, 4, 5]
# # doubled = list(map(lambda x: x * 2, numbers))
# # print(doubled)

# # Task 2.Use map() to convert the list ["1", "2", "3", "4"] into integers.
# # mylist= ["1", "2", "3", "4"]
# # def myfun(a):
# #     return a
# # res= tuple(map(myfun,mylist))
# # print(res)

# # Task 3.Use map() to convert the list ["apple", "banana", "mango"] into uppercase letters.
# # mylist =["apple", "banana", "mango"] 
# # res=tuple(map(lambda x:x.upper(),mylist))
# # print(res)

# # Task4.Use map() to find the length of each word in the list ["cat", "dog", "fish"].
# # mylist =["cat", "dog", "fish"]
# # lengths = list(map(len, mylist))
# # print(lengths)

# # Task5.Use map() to add 10 to each number in the list [5, 10, 15, 20].
# # mylist= [5, 10, 15, 20]
# # def add(a):
# #     return a+10
# # res=list(map(add,mylist))
# # print(res)


# # Filter method

# # Task1.Write a program to filter all even numbers from a list.   
# # numbers = [12, 5, 18, 7, 25, 9]
# # def even(a):
# #     return a%2==0
# # res=list(filter(even,numbers))
# # print(res)


# # Task 2.Filter all odd numbers from a list.
# # numbers = [12, 5, 18, 7, 25, 9]
# # res=list(filter(lambda x:x%2!=0,numbers))
# # print(res)

# # Task3.Filter all positive numbers from a list.
# numbers = [10, -3, 25, -8, 0, 14, -19, 7, -2, 6]
# res=list(filter(lambda x:x>=0,numbers))
# print(res)

# # Task4.Filter all negative numbers from a list.
# numbers = [10, -3, 25, -8, 0, 14, -19, 7, -2, 6]
# res=list(filter(lambda x:x<0,numbers))
# print(res)

# # Task 5.Filter all numbers greater than 50.
# numbers = [45, 12, 89, 3, 67, 100, 28, 91, 54, 6, 73, 19]
# def greater(a):
#     return a>50
# res=list(filter(greater,numbers))
# print(res)


# reduce 

# Task1. Use reduce() to find the *sum* of all elements in a list of integers.
# numbers = [12, 5, 18, 7, 25, 9]
# def add_red(x,y):
#     return x+y
# res=reduce(add_red,numbers)
# print(res)


# Task2. Use reduce() to find the *product* of all elements in a list of integers.
# numbers = [12, 5, 18, 7, 25, 9]
# def pro_red(x,y):
#     return x*y
# res=reduce(pro_red,numbers)
# print(res)


# Task3. Use reduce() to find the *largest element* in a list.
# numbers = [12, 5, 18, 7, 25, 9]
# largest = reduce(lambda x, y: x if x > y else y, numbers)
# print(largest)


# Task4. Use reduce() to *concatenate* all strings in a list into a single string.
# words = ["Hello", " ", "World", "!"]
# result = reduce(lambda x, y: x + y, words)
# print(result)

# Task 5. Use reduce() to find the *total number of characters* in a list of strings.
# mylist=["I" "love" "python"]
# res=reduce(lambda x,y:x+len(y),mylist,0)
# print(res)

# one shot 
# Task 1. Use map() to triple each number in a list of integers.
# mylist=[1,2,3,4,5]
# res=list(map(lambda a:a*3,mylist))
# print(res)

# Task2. Use map() to convert all strings to lowercase in a list of words.
# mylist =["APPLE", "BANANA", "MANGO"] 
# res=tuple(map(lambda x:x.lower(),mylist))
# print(res)

# Task 3 Use reduce() to find the minimum element in a list of integers.

numbers = [12, 5, 18, 7, 25, 9]
smallest = reduce(lambda x, y: x if x < y else y, numbers)
print(smallest)


# Task4. Use reduce() to join all words with spaces into one sentence.
words = ["Hello", "world.", "This", "is", "Python"]
sentence = reduce(lambda x, y: x + " " + y, words)
print(sentence)

# Task5. Filter all numbers that are multiples of 3 from a list.
numbers = [12, 45, 7, 89, 23, 56, 3, 78]
res=list(filter(lambda x:x%3==0,numbers))
print(res)

# Task6. Filter all strings that start with a vowel from a list of words.
words = ["apple", "banana", "orange", "grape", "umbrella", "elephant"]
vowels = "aeiou"
result = list(filter(lambda word: word[0].lower() in vowels, words))
print(result)