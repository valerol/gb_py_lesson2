# Task 3
import random

someList = list(input("Print something "))

for elem in someList:
    someList.insert(random.randrange(0, len(someList)), someList.pop(someList.index(elem)))

print(''.join(str(elem) for elem in someList))