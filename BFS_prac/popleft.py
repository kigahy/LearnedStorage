from collections import deque

mySet = deque()
mySet.append((1, 2))
x, y = mySet.popleft()

print(x, y)
print(type(mySet))