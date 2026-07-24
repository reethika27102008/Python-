# PUblic attribute
# class employee:
#     def __init__(self,name,age):
#         self.name=name 
#         self.age=age
# objemployee=employee("Sam",23)
# print(objemployee.age)
# print(objemployee.name)


# PROTECTED ATTRIBUTE
# class parent():
#     def __init__(self,name,age):
#         self._name=name
#         self._age=age
# class child(parent):
#     def show_age(self):
#         print(self._age)
#     def show_name(self):
#         print(self._name)

# obj_child=child("Sam",23)
# # obj_child.show_age()
# # obj_child.show_name()
# # obj_child._age
# print(obj_child._age)

# PRIVATE ATTRIBUTE
class employee:
    def __init__(self,name,age):
        self.__name=name

    def show_name(self):
        print(self.__name)

obj=employee("Sam",23)
# obj.__name
obj.show_name()



# encapsulation - bundling of data and method
# private
# protected
# public

# public
# class employee:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# obj=employee("sam",23)
# print(obj.name)
# print(obj.age)


# Protected
# class parent:
#     def __init__(self ,name,age):
#         self._name=name
#         self._age=age

# class child(parent):
#     def show_age(self):
#         print(self._name)

# objchild=child("sam",23)
# objchild.show_age()
# print(objchild._age)

# private

# class employee:
#     def __init__ (self,name,age):
#         self.__name=name
#         self.__age=age

# obj=employee("sam",23)
# print(obj.__age)






