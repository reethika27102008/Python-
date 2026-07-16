#task1 zero Division error 
# try:
#     n = int(input("Enter your number: "))
#     divide = n /200
#     print( divide)
# except ZeroDivisionError:
#     print("A number cannot be divided by zero.")
# except ValueError:
#     print("Please enter valid integers.")
# else:
#     print("There is no error in the try block.")
# finally:
#     print("Execution completed successfully.")

# #task2 Name error
# try:
#     print(value)
#     add(23,90)
# except NameError:
#     print("Variable or function name is not defined.")
# else:
#     print("There is no error in the try block")
# finally:
#     print("Execution completed successfully")

# #task3 Type error
# try:
#     print("one"+2)
# except TypeError:
#     print("You cannot add two types of datatype")
# else:
#     print("There is no error in the try block")
# finally:
#     print("Execution completed successfully")

# #task4 value error
# try:
#     n=int(input("Enter your value:"))
#     print(n)
# except ValueError:
#     print("Please enter a valid integer")
# else:
#     print("There is no error in the try block")
# finally:
#     print("Execution completed successfully")

# # task5 keyerror
# try:
#     student = {"name": "Alice", "age": 20}
#     print(student["marks"])
# except KeyError:
#     print("Key not found in the dictionary.")
# else:
#     print("There is no error in the try block")
# finally:
#     print("Execution completed successfully")

# # task6
# try:
#     file = open("student.txt", "r")
#     print(file.read())
#     file.close()
# except FileNotFoundError:
#     print("File not found.")
# else:
#     print("There is no error in the try block")
# finally:
#     print("Execution completed successfully")


# #task 7 import error
try:
    from math import square
except ImportError:
    print("Cannot import 'square' from the math module.")
else:
    print("There is no error in the try block")
finally:
    print("Execution completed successfully")