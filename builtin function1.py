from functools import reduce
# Task 1 Double All Numbers

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# Task 2 Square All Numbers
numbers = [2, 3, 4, 5]
square = list(map(lambda x: x * x, numbers))
print(square)

# Task 3 Convert Strings to Integers
mylist= ["10", "20", "30", "40"]
Integers=list(map(lambda x:int(x),mylist))
print(Integers)

# Task 4 Convert Names to Uppercase
name=["john", "alice", "bob"]
res=tuple(map(lambda x:x.upper(),name))
print(res)

# Task 5 Find Length of Each Word
length=["apple", "banana", "kiwi"]
res=tuple(map(lambda x:len(x),length))
print(res)

# Task 6. Filter Even Numbers
even=[1, 2, 3, 4, 5, 6]
res=tuple(filter(lambda x :x%2==0,even))
print(res)

# Task 7. Filter Odd Numbers
odd=[1, 2, 3, 4, 5, 6]
res=list(filter(lambda x :x%2!=0,odd))
print(res)

# Task 8.Filter Positive Numbers
num=[-5, -2, 0, 3, 8]
res=list(filter(lambda x:x>=0,num))
print(res)

# Task 9 Filter Words Longer Than 4 Characters
animals=["cat", "elephant", "dog", "tiger"]
res=list(filter(lambda x:len(x)>4,animals))
print(res)

# Task 10. Extract Vowels from a String
string="programming"
vowels="aeiou"
res=list(filter(lambda x:x in vowels,string))
print(res)

# Task 11. Sum of all Numbers
num=[1, 2, 3, 4, 5]
res=reduce(lambda x,y:x+y,num)
print(res)


# Task 12. Product of All Numbers
num=[1, 2, 3, 4]
res=reduce(lambda x,y:x*y,num)
print(res)

# Task 13. Find Maximum Number
num=[4, 10, 7, 25, 3]
maximum = reduce(lambda x,y: max(x,y), num)
print(maximum)

# Task 14. Find Minimum Number
num=[4, 10, 7, 25, 3]
minimum= reduce(lambda x, y: min(x,y), num)
print(minimum)

# Task 15  Join Words into a Sentence
string=["Python", "is", "awesome"]
sentence=reduce(lambda x,y:x+" "+y,string)
print(sentence)

# Task 16. Square Only Even Numbers
num = [1, 2, 3, 4, 5, 6]
square = list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, num)))
print(square)

# Task17.Sum of Even Numbers
num=[1, 2, 3, 4, 5, 6]
add=reduce(lambda x,y: x+y,filter(lambda x:x%2==0,num))
print(add)

# Task 18 Count Words with Length Greater Than 3
words = ["cat", "apple", "dog", "banana"]
count = len(list(filter(lambda x: len(x) > 3, words)))
print(count)

# Task 19. Sum of Squares of Odd Numbers
num = [1,2,3,4,5]
result = sum(map(lambda x:x**2,filter(lambda x:x%2!=0,num)))
print(result)
# or
# num = [1,2,3,4,5,]
# result = (reduce(lambda x,y:x+y,map(lambda x:x**2,filter(lambda x:x%2!=0,num))))
# print(result)


# Task 20. Sum of Cubes of Even Numbers

num = [1,2,3,4,5,6]
result = sum(map(lambda x:x**3,filter(lambda x:x%2==0,num)))
print(result)
# or
# num = [1,2,3,4,5,6]
# result = (reduce(lambda x,y:x+y,map(lambda x:x**3,filter(lambda x:x%2==0,num))))
# print(result)
