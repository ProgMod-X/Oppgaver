import random

list = []

print(list)
for i in range(5):
    list.append(random.randint(20,80))
    print(list)

for i in range(5):
    list.pop(0)
    print(list)
    # print(list[i:])