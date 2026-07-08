from modules1 import *
# print(amount)
print(name)
print(add(10,3))

import modules1
print(modules1.name)
# print(modules1.amount)
# print(modules1.add(10,3))

from modules1 import amount,name,add
# print(amount)
print(name)
print(add(10,3))

import modules1 as m1
print(m1  .name)
print(m1.amount)
print(m1.add(10,3))