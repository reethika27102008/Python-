# CLASS 
# # class A:
#     message="Hello World!"
#     def f1(self):
#         print("message")

# object=A()
# print(object.message)
# print(object.f1())
# print(object.f1)

# INHERITANCE
# # Type1 Single Inheritance
# class Parent:
#     def f1(self):
#         print("parent class fun is working")
# class Child(Parent):
#     def f2(self):
#         print("Child class func is working")

# childObj = Child()
# childObj.f1()
# childObj.f2()

# #  Type 2 Multiple Inheritance
# class Father:
#     def f1(self):
#         print("GrandParent class func is working")
# class Mother:
#     def f2(self):
#         print("Mother class func is working")
# class Child(Father, Mother):
#     def f3():
#         print("Child class function is working")
    

# # Type 3 Multilevel Inheritance
# class grandparent:
#     def f1(self):
#         print("GrandParent class func is working")
# class father(grandparent):
#     def f2(self):
#         print("Father class func is working")
# class child(father):
#     def f3():
#         print("Child class function is working")

# objectchild=child()
# objectchild.f2

# # Type 4 Hierarchical Inheritance
# class Parent:
#     def f1(self):
#         print("Parent class func is working")
# class Child1(Parent):
#     def f2(self):
#         print("child1 class func is working")
# class Child2(Parent):
#     def f3():
#         print("Child2 class function is working")

# objectchild=Child2()
# objectchild.f3

# OVERLOADING 

# class animal():
#     def cat(self):
#         print("Meow")
#     def cat(self):
#         print("BARK")

# objani=animal()
# objani.cat()

# using a default parameter.

# class Animal:
#     def cat(self, sound="Meow"):
#         print(sound)
# obj = Animal()
# obj.cat()
# obj.cat("BARK")

# OVERRIDING

# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self):
#         super().sound()   
#         print("Dog barks")

# obj = Dog()
# obj.sound()


# encapsulation
# public attribute

# class encap:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary

# emp=encap("Sam",5000)
# print(emp.name)
# print(emp.salary)

# class encap:
#     def __init__(self,name,salary):
#         self.name=name
#         self.__salary=salary

# emp=encap("Sam",5000)
# print(emp.name)
# print(emp.__salary)

class parent:
    def __init__(self,name,age):
        self.name=name
        self._age=age
class child(parent):
    def show_age(self):
        print(self._age)

objchild=child("Sam",23)
objchild.show_age()
print(objchild.name)
