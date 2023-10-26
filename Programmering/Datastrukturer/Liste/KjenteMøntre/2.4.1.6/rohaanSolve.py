import random

list = []

print(list)
for i in range(5):
    list.append(random.randint(20,80))
    print(list)

for i in range(5):
    list.pop()
    print(list)