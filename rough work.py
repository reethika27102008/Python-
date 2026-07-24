# def language():
#     return "Python"
#     print("Java")
# print(language())

# # class Student:
# #     def _init_(self, n):
# #         self.name = name

# #     def display(self):
# #         print("Name:", self.name)

# # s1 = Student("Alice")
# # s2 = Student("Reethika")
# # s1.display()
# # s2.display()


class Employee:
    def __init__(self, name, salary):
        self.name = name          # public
        self.__salary = salary    # private

    def show_salary(self):
        print("Salary:", self.__salary)

emp = Employee("Robert", 60000)
# print(emp.name)          # Public accessible
emp.show_salary()        # Accessing private correctly
# print(emp.__salary)    # Error: Not accessible directly