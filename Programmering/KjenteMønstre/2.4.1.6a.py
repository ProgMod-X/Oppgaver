import random

stack = []

print("Legger til i stacken")
for i in range(5):
    stack.append(random.randint(20,80))
    print(stack[i])