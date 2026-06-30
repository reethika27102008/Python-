#  task1  Given two lists, return the set of common elements 
# that appear more than once in both lists.

set1={10,20,30,40,60}
set2={0,2,3,40,50,60,70}
print(set1.intersection(set2))

# task2. Create a set of unique words from a sentence, where words are separated 
# by spaces and punctuation marks should be ignored.

# sentence = input("Enter a sentence: ")
# cleaned = ""
# for i in sentence:
#     if i.isalnum() or i.isspace():
#         cleaned += i
# unique_words = set(cleaned.split())
# print("Unique words:", unique_words)

# Task3. Write a function that takes a list of numbers and returns 
# the largest subset such that the sum of the subset is even.

# total = 0
# myset = {2, 87, 34, 98, 67}
# for i in myset:
#     total += i
# print("Original set:", myset)
# smallest = 100
# if total % 2 != 0:
#     for i in myset:
#         if i % 2 != 0 and i < smallest:
#             smallest = i
#     myset.remove(smallest)
#     print("Result:", myset)


# Task 5. Check if two sets are equal, considering their elements but ignoring
#  the order (i.e., set equality).
# set1={23,54,87,54,34,98}
# set2={23,54,87,54,34,98}
# def equal (result):
#     if set1==set2:
#         print("The two sets are equal")
#     else: 
#         print("The two sets are not equal")
# equal(set1)

# Task Find the set difference of multiple sets.
# A = {1, 2, 3, 4, 5}
# B = {2, 4}
# C = {5}
# result = A - B - C
# print("Set Difference:", result)

# 6. Write a program that finds the intersection of multiple sets.
# set1={67,54,90,87,89}
# set2={34,98,78,67,90,89}
# set3={54,90,89}
# print(set1.intersection(set2,set3))

# Task14. Write a function to determine whether a set is a proper subset of another set.
# set1={23,45,22,56,}
# set2={23,45,22,56,21,32,11}
# print(set1.issubset(set2))

# 20. Write a function that finds the union of all sets,
#  but only includes elements that appear more than once across all sets.

# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# set3 = {3, 5, 6}
# uniondata=set1.union(set2,set3)
# print("Union set  =",uniondata)


# 12. Given two sets, find the symmetric difference, but only include elements that
#  appear more than once across both sets.

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# result = set1.symmetric_difference(set2)
# print("Symmetric Difference =", result)

# 17. Create a set of all permutations of a given list of characters.


# from itertools import permutations
# myset = ['a', 'b', 'c']
# new_set = set(permutations(myset))
# print(new_set)