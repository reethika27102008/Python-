# Task 1
# for i in range( 5):  
#     for j in range( i + 1):      
#       print("*", end=" ")   
#     print() 

# Task2
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# # Task3
rows = int(input("Enter the row size for the pattern: "))
for i in range(1, 6):  
    for j in range(6 - i):  
        print(" ", end=" ")
    for k in range(1, 2 * i):  
        print("*", end=" ")
    print()

# Task4 
    
# for i in range(5, 0, -1):  
#     for j in range(5  - i):    
#          print(" ", end=" ")
#     for k in range(1, 2 * i):  
#         print("*", end=" ")
#     print()  

# Task5


# for i in range(1,6): 
#     for j in range(6  - i):
#         print(" ", end=" ")
#     for k in range(1, 2 * i):
#         print("*", end=" ")
#     print()
# for i in range(6- 1, 0, -1):  
#     for j in range(6 - i):
#         print(" ", end=" ")
#     for k in range(1, 2 * i):
#         print("*", end=" ")
#     print()

# Task6

# for i in range(1, 6):  # Outer loop for rows
#     for j in range(1, 6):  # Inner loop for columns
#         if i == 1 or i == 5 or j == 1 or j == 5 :  # Print star only on borders
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")  # Print space inside
#     print()

# Task7 

# rows = int(input("Enter the row size for the pattern: "))
# for i in range(1, 6):  # Outer loop for rows
#     for j in range(1, i + 1):  # Inner loop for columns
#         if j == 1 or i == 5 or i == j:  # Print star on borders
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")  # Print space inside
#     print()


# Task 8


# rows = int(input("Enter the row size for the pattern:"))
# for i in range(rows , 0, -1):  # Outer loop for rows in reverse
#     for j in range(1, i + 1):  # Inner loop for columns
#         if j == 1 or i == rows or i == j:  # Print star on borders
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")  # Print space inside
#     print()  # Move to the next line


# Task9

# rows = int(input("Enter the row size for the pattern: "))
# for i in range(1, rows + 1):  # Outer loop for rows
#     for j in range(rows  - i):  # Inner loop for spaces
#         print(" ", end=" ")
#     for k in range(1, 2 * i):  # Inner loop for stars
#         if k == 1 or k == 2 * i - 1 or i == rows:  # Print star on borders
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")  # Print space inside
#     print()
    

# Task 10

# rows = int(input("Enter the row size for the pattern: "))
# for i in range(rows, 0, -1):  # Outer loop for rows in reverse
#     for j in range(rows - i):  # Inner loop for spaces
#         print(" ", end=" ")
#     for k in range(1, 2 * i):  # Inner loop for stars
#         if k == 1 or k == 2 * i - 1 or i == rows:  # Print star on borders
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")  # Print space inside
#     print()