import random
from collections import Counter
import math
from collections import defaultdict
from collections import deque

data=random.randint(0,100)
print(data)

data1=random.random()
print(data1)

data2=random.uniform(5,8)
print(data2,"random.random")

myList = [23,569,2,93,16,9,2,67]
print(random.choice(myList))
random.shuffle(myList)
print(myList)

a=(23,87,90,56)
print(random.sample(a,2))

b=[1,24,78,79,56,54,32,21,90]
print(random.sample(b,4))

c="34768956432315"
print(random.sample(c,2))

numbers = [3,3,5,7,34,8,2,5,5,2,8,23,12,67]
print(Counter(numbers))

print(math.ceil(17.5))
print(math.ceil(2.1))
print(math.floor(5.7))
print(math.ceil(2.0))
print(math.sqrt(25))
print(math.pow(2,10))

print(max(myList))
print(min(myList))
print(round(5.1))
print(abs(-50))

d= defaultdict(int)
d["apple"] += 10
d["banana"] += 20
print(d)

dq = deque([1, 2, 3])
dq.append(10)
dq.appendleft(4)
print(dq)


dq.pop()
dq.popleft()
print(dq)